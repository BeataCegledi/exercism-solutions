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
        for i_char, char in enumerate(row):
            if char == '*':
                new_row += '*'
            else:                
                value = sum(1 for neighbor_x, neighbor_y in neighbors 
                            if 0 <= i_row+neighbor_x < len(garden)
                            and 0 <= i_char+neighbor_y < len(row)
                            and garden[i_row+neighbor_x][i_char+neighbor_y] == '*')
                new_row += str(value) if value > 0 else ' '
        result.append(new_row)
    return result

    
