'''Series of substrings of given length.'''

def slices(series, length):
    '''Return all contiguous substrings of `series` with given `length`.'''
    
    if length == 0:
        raise ValueError("slice length cannot be zero")
    if length < 0:
        raise ValueError("slice length cannot be negative")
    if series == "":
        raise ValueError("series cannot be empty")
    if length > len(series):
        raise ValueError("slice length cannot be greater than series length")

    return [series[index:index+length] for index in range(len(series)-length+1)]