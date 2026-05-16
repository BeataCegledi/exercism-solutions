'''Build the rows of a diamond made of letters.'''

def rows(letter):
    '''Return the diamond for `letter` as a list of strings.

    Each row is the same length, padded with spaces so the letters form
    a diamond shape with 'A' at the top and bottom and `letter` in the
    middle. For example, rows('C') returns:
    ['  A  ', ' B B ', 'C   C', ' B B ', '  A  '].'''
    middle = ord(letter.upper())-ord('A')
    size = 2 * middle + 1
    diamond = []
    for vertical in range(middle +1):
        row = [' '] * size
        current_letter = chr(ord('A')+vertical)
        row[middle - vertical] = current_letter
        row[middle + vertical] = current_letter
        diamond.append(''.join(row))
    diamond = diamond + diamond[-2::-1]
    return diamond
