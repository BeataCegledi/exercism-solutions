'''Rail fence cipher encoder and decoder.'''

def encode(message, rails):
    '''Encode message using the rail fence cipher with given rails.'''
    
    if rails == 1:
        return message
    result = [''] * rails
    row, direction = 0, -1
    for char in message:
        result[row] += char
        if row in (0, rails - 1):
            direction = -direction
        row += direction
    return ''.join(result)

def decode(encoded_message, rails):
    '''Decode a rail fence cipher message with given rails.'''
    
    if rails == 1:
        return encoded_message
    counts = [0] * rails
    row, direction = 0, -1
    for _ in range(len(encoded_message)):
        counts[row] += 1
        if row in (0, rails - 1):
            direction = -direction
        row += direction
    rows = [''] * rails
    start = 0
    for index in range(rails):
        rows[index] = encoded_message[start:start + counts[index]]
        start += counts[index]
    row, direction = 0, -1
    indexer = [0] * rails
    result = ''
    for index in range(len(encoded_message)):
        result += rows[row][indexer[row]]
        indexer[row] += 1
        if row in (0, rails - 1):
            direction = -direction
        row += direction
    return result