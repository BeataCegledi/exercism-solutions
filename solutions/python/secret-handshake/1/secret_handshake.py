def commands(binary_str):
    """Decode a 5-bit binary string into a list of secret handshake actions.

    Bits 1–4 (right to left) encode: jump, double blink, close your eyes, wink.
    Bit 0 (leftmost) reverses the final order if set.

    :param binary_str: 5-character binary string, e.g. '10011'
    :return: list of action strings in the correct order
    """
    
    actions = ['wink', 'double blink', 'close your eyes', 'jump']
    handshake = [
        action
        for action, bit in zip(actions, binary_str[4:0:-1])
        if bit == '1'
    ]
    
    if binary_str[0] == '1':
        handshake.reverse()
    return handshake