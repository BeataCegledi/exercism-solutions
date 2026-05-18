'''Convert an OCR grid of pipes, underscores, and spaces into a digit string.'''
DIGITS = {
    ' _ :| |:|_|:   ': '0',
    '   :  |:  |:   ': '1',
    ' _ : _|:|_ :   ': '2',
    ' _ : _|: _|:   ': '3',
    '   :|_|:  |:   ': '4',
    ' _ :|_ : _|:   ': '5',
    ' _ :|_ :|_|:   ': '6',
    ' _ :  |:  |:   ': '7',
    ' _ :|_|:|_|:   ': '8',
    ' _ :|_|: _|:   ': '9',
}
def convert(input_grid):
    '''Return the digits encoded in the OCR grid.

    Each cell is 3 columns wide and 4 rows tall. Rows of cells are
    separated by ',' in the output. Unrecognized cells become '?'.
    Raises ValueError if the grid dimensions are invalid.'''
    
    result = ''
    if len(input_grid) % 4 != 0:
        raise ValueError('Number of input lines is not a multiple of four')
    if any(len(row) % 3 != 0 for row in input_grid):
        raise ValueError('Number of input columns is not a multiple of three')
    if any(len(row) != len(input_grid[0]) for row in input_grid):
        raise ValueError('Invalid size')
    for row in range(0, len(input_grid), 4):
        if row > 0:
            result += ','
        for column in range(0, len(input_grid[0]), 3):
            parts = [input_grid[row + i][column:column + 3] for i in range(4)]
            current = ':'.join(parts)
            if current in DIGITS:
                result += DIGITS[current]
            else:
                result += '?'
    return result