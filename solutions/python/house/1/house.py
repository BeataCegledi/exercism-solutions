def recite(start_verse, end_verse):
    '''Return verses from the cumulative rhyme 'The House That Jack Built'.

    Verses are numbered starting from 1. The function returns all verses
    from start_verse to end_verse, inclusive.
    '''
    
    verbs = ['lay in', 'ate', 'killed', 
             'worried', 'tossed', 'milked', 
             'kissed', 'married', 'woke', 
             'kept', 'belonged to']
    sentences = ['the house that Jack built',
                 'the malt',
                 'the rat',
                 'the cat',
                 'the dog',
                 'the cow with the crumpled horn',
                 'the maiden all forlorn',
                 'the man all tattered and torn',
                 'the priest all shaven and shorn',
                 'the rooster that crowed in the morn',
                 'the farmer sowing his corn',
                 'the horse and the hound and the horn']
    
    verse = []
    
    for verse_index in range(12):
        verse.append(f'This is {sentences[verse_index]}')
        for line_index in range(verse_index-1,-1,-1):
            verse[verse_index] += f' that {verbs[line_index]} {sentences[line_index]}'
        verse[verse_index] += ('.')
    return verse[start_verse-1:end_verse]