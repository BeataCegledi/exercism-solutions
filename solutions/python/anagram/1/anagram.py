def find_anagrams(word, candidates):
    """Find all anagrams of a target word from candidate list.
    
    Args:
        word (str): The target word.
        candidates (list): List of candidate words to check.
    
    Returns:
        list: Anagrams (case-insensitive, original case preserved).
    """
    result = [is_anagram for is_anagram in candidates 
              if sorted(word.upper()) == sorted(is_anagram.upper())]
    return [isequal for isequal in result if isequal.upper() != word.upper()]
    
            
