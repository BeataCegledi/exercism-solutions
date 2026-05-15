'''Atbash cipher: maps each letter to its mirror (a↔z, b↔y, ...).'''

ABC = 'abcdefghijklmnopqrstuvwxyz'
ATBASH = str.maketrans(ABC, ABC[::-1])


def encode(plain_text):
    '''Encode text with Atbash, grouped into blocks of 5 chars.'''
    encoded = ''
    count = 0
    for char in plain_text.lower():
        if char.isalpha():
            encoded += char.translate(ATBASH)
            count += 1
        elif char.isdigit():
            encoded += char
            count += 1
        else:
            continue
        if count % 5 == 0:
            encoded += ' '
    return encoded.strip()


def decode(ciphered_text):
    '''Decode an Atbash-ciphered text, ignoring spaces.'''
    decoded = ''
    for char in ciphered_text:
        if char.isalpha():
            decoded += char.translate(ATBASH)
        elif char.isdigit():
            decoded += char
    return decoded
    