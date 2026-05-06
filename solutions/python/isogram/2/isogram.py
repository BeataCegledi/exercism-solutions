def is_isogram(string):
    """Determines if a word or phrase is an isogram."""
    string = string.lower().replace(" ","").replace("-","")   
    return len(string) == len(set(string))
    