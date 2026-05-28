"""Recite the 'Ten Green Bottles' song."""

def recite(start, take=1):
    """Return lines of the song starting from `start` for `take` verses.
    Args:
        start: Number of bottles in the first verse (1-10).
        take: How many verses to return.
    Returns:
        List of strings, one per line, with blank lines between verses.
    """
    
    number = ['no', 'One', 'Two', 'Three', 'Four', 'Five',
         'Six', 'Seven', 'Eight', 'Nine', 'Ten']
    result = []
    
    for verses in range(take):
        
        minus = number[start-1].lower()
        more  = '' if start == 1 else 's'
        more1 = '' if start == 2 else 's'
        row1 = f"{number[start]} green bottle{more} hanging on the wall," 
        row3 = f"And if one green bottle should accidentally fall,"
        row4 = f"There'll be {minus} green bottle{more1} hanging on the wall."

        if verses > 0:
            result.append("")
        result.extend([row1, row1, row3, row4])
        start -= 1
    return result
