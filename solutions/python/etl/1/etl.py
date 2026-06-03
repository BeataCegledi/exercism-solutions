"""Legacy score data conversion."""
def transform(legacy_data):
    """Flatten {point: [letters]} into {letter: point} with lowercase keys.
    Args: legacy_data: dict mapping int points to lists of letter strings.
    Returns: dict mapping each lowercase letter to its point value."""
    
    return  {letter.lower() : point 
             for point, letters in legacy_data.items() 
             for letter in letters}
