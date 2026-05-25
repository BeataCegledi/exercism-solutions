'''Variable Length Quantity encoding and decoding.'''


def encode(numbers):
    '''Encode integers into a VLQ byte sequence.
    
    Args: numbers: Iterable of non-negative 32-bit integers.
    Returns: List of bytes representing the VLQ-encoded numbers.'''
    
    result = []
    for number in numbers:
        if number == 0:
            result.append(0)
            continue
        vlq = []
        current = number
        while current:
            vlq.append((current % 0x80) | 0x80)
            current >>= 7
        vlq[0] &= 0x7F
        result.extend(vlq[::-1])
    return result


def decode(bytes_):
    '''Decode a VLQ byte sequence into integers.

    Args: bytes_: Iterable of bytes in VLQ format.
    Returns: List of decoded integers.
    Raises: ValueError: If the sequence is incomplete (last byte has MSB set). '''
    
    result = []
    current = 0
    end_flag = True
    for byte in bytes_:
        current = (current << 7) | (byte & 0x7F)
        end_flag = False
        if not byte & 0x80:
            result.append(current)
            current = 0
            end_flag = True
    if not end_flag:
        raise ValueError('incomplete sequence')
    return result