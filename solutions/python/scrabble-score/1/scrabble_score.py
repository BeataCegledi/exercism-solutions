"""Scrabble word scoring."""

def score(word):
    """Calculate the Scrabble score of a word.
    Args:    word: word to score (case-insensitive).
    Returns: int total point value. """
    
    POINTS = {"AEIOULNRST": 1, "DG": 2, "BCMP": 3,"FHVWY": 4, "K": 5, "JX": 8, "QZ": 10}
    
    points_new = {letter: point for letters, point in POINTS.items() for letter in letters}
    return sum(points_new.get(ch, 0) for ch in word.upper())