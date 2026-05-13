def square_root(number):
    """Return the integer square root of a perfect square."""
    
    return next(root for root in range(number+1) if root * root == number)
