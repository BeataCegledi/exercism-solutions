def largest_product(series, size):
    """Largest product of consecutive digits in a string.
    
    Args:
        series: String of digits.
        size: Length of the span.
        
    Raises:
        ValueError: If size exceeds string length, is negative, or series contains non-digits.
    """
    if size > len(series):
        raise ValueError("span must not exceed string length")
    elif size < 0:
        raise ValueError("span must not be negative")
    elif not series.isdecimal():
        raise ValueError("digits input must only contain digits")
    largest = 0
    for index in range(len(series)-size+1):
        serie = series[index:(index+size)]
        produkt = 1
        for ch in serie:
            produkt *= int(ch)
        if produkt > largest:
            largest = produkt
    return largest      
