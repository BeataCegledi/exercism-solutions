"""Find saddle points in a matrix — points that are row max and column min."""

def saddle_points(matrix):
    """Find all saddle points in a matrix.
    # A saddle point: row maximum AND column minimum simultaneously
    # Irregular matrix raises ValueError
    # Returns list of dicts: [{"row": int, "column": int}, ...]
    """
    
    if (not matrix or not matrix[0]):
        return []
    result = []
    cmin = []
    for _ in range(len(matrix[0])):
        cmin.append(float("inf")) 
        
    for row in range(len(matrix)):
        if len(matrix[row]) != len(matrix[0]):
            raise ValueError("irregular matrix")
        for column in range(len(matrix[0])):
            if cmin[column] > matrix[row][column]:
                cmin[column] = matrix[row][column]

    for row in range(len(matrix)):
        rmax = max(matrix[row])
        for column in range(len(matrix[0])):
            if rmax == matrix[row][column] and cmin[column] == matrix[row][column]:
                result.append({"row": row+1, "column": column+1})
    
    return result
                    
        
