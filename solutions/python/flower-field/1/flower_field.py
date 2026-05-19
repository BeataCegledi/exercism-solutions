'''Flower Field: annotate empty squares with adjacent flower counts.'''
def annotate(garden):
    '''Replace empty squares in the garden with adjacent flower counts. Each  empty square becomes the number of flowers in its neighboring cells. Empty and flower squares stays unchanged.

Args:    garden: List of equal-length strings containing only ' ' and '*'.

Returns: New list of strings with counts filled in.

Raises:  ValueError: If rows differ in length or contain invalid characters.'''
    
    if not garden:
        return []
    if any(char not in ' *' for row in garden for char in row) or any(len(row) != len(garden[0]) for row in garden):
        raise ValueError('The board is invalid with current input.')    
        
    neighbors = [(-1,-1), (-1,0), (-1,1),
              ( 0,-1),         ( 0,1),
              ( 1,-1), ( 1,0), ( 1,1)]
    result = []
    for i_row, row in enumerate(garden):
        new_row = ''
        for i_char in range(len(row)):
            if row[i_char] == '*':
                new_row += '*'
            else:                
                value = 0
                for neighbor_x, neighbor_y in neighbors:
                    n_row = i_row + neighbor_x
                    n_char = i_char + neighbor_y
                    if 0 <= n_row < len(garden) and 0 <= n_char < len(row):
                        if garden[n_row][n_char] == '*':
                            value += 1
                new_row += str(value) if value > 0 else ' '
        result.append(new_row)
    return result

    
