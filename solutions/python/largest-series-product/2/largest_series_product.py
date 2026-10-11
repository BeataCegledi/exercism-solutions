def largest_product(series, size):
    """Largest product of consecutive digits in a string.
    
    Args:
        series: String of digits.
        size: Length of the span.
        
    Raises:
        ValueError: If size exceeds string length, is negative, or series contains non-digits.
    """
    def get_product(serie):
        product = 1
        for digit in serie:
            product *= int(digit)
        return product
    
    if size > len(series):
        raise ValueError("span must not exceed string length")
    if size < 0:
        raise ValueError("span must not be negative")
    if not series.isdecimal():
        raise ValueError("digits input must only contain digits")
    
    return max(get_product(series[index:index+size]) for index in range(len(series) - size + 1))    
