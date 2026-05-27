'''Classic method for composing secret messages called a square code'''

def cipher_text(plain_text):
    '''Encode text using the classic square code cipher.

    Args: 
        plain_text: Raw input string (any case, with punctuation).
    Returns: 
        Encoded string: columns read top-to-bottom, separated by spaces.'''
    
    normalized = ''.join(char.lower() for char in plain_text if char.isalnum())
    columns = int(len(normalized) ** 0.5)
    if columns * columns < len(normalized):
        columns += 1
    if columns <= 1:
        return normalized
    rows = -(-len(normalized) // columns)       
    normalized = normalized.ljust(rows * columns)
    return ' '.join(normalized[column::columns] for column in range(columns))
