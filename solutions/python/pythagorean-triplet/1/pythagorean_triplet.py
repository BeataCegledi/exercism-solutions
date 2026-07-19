"""Find all Pythagorean triplets that sum to a given number."""

def triplets_with_sum(number):
    """Find Pythagorean triplets (a, b, c) where: 
    # a + b + c = number
    # a**2 + b**2 = c**2
    # a < b < c
    """
    
    triplets = []
    for a in range(1, number // 3):
        a_square = a * a
        b_max = (number - a) // 2
        for b in range(a + 1, b_max + 1):
            c = number - a - b
            b_square = b * b
            if a_square + b_square == c * c:
                triplets.append([a, b, c])
    return triplets