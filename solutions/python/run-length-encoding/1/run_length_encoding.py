'''Run-length encoding and decoding.'''

def decode(string):
    '''Decode a run-length encoded string.'''
    result = ''
    count = ''
    for char in string:
        if char.isdigit():
            count += char
        else:
            result += char * (int(count) if count else 1)
            count = ''
    return result


def encode(string):
    '''Run-length encode a string.'''
    
    if not string:
        return ''
    count = 1
    last = string[0]
    result = ''
    for char in string[1:]:
        if char != last:
            if count > 1:
                result += str(count)
            result += last                           
            last = char            
            count = 1
        else:
            count += 1
    if count > 1:
        result += (str(count))
    result += last
    return result