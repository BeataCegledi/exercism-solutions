'''Conway's Game of Life.'''
NEIGHBORS = [(-1,-1), (-1,0), (-1,1),
             ( 0,-1),         ( 0,1),
             ( 1,-1), ( 1,0), ( 1,1)]

def tick(matrix):
    '''Return the next generation of the grid.'''
    if not matrix or not matrix[0]:
        return matrix
    rows, cols = len(matrix), len(matrix[0])
    result = [[0] * cols for index in range(rows)]
    for row in range(rows):
        for column in range(cols):
            count_neigh = sum(matrix[row + neighrow][column + neighcol] 
                              for neighrow, neighcol in NEIGHBORS
                              if 0 <= row + neighrow < rows 
                              and 0 <= column + neighcol < cols )
            if count_neigh == 3 or (matrix[row][column] == 1 and count_neigh == 2):
                result[row][column] = 1
    return result