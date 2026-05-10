def distance(strand_a, strand_b):
    '''Return the Hamming distance between two equal-length strings.
    
    :param strand_a: First string
    :param strand_b: Second string
    :return: Number of differing character positions
    :raises ValueError: If the strings are of unequal length'''
    
    if len(strand_a) != len(strand_b):
        raise ValueError('Strands must be of equal length.')
    return sum(letter_a != letter_b for letter_a, letter_b in zip(strand_a, strand_b))
        
