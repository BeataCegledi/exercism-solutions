def recite(start_verse, end_verse):

    """
    Generate verses from the song 'The Twelve Days of Christmas'.

    Args:
        start_verse (int): The starting verse number (1-based).
        end_verse (int): The ending verse number (1-based).

    Returns:
        list[str]: A list of verses from start_verse to end_verse (inclusive).
    """

    numbers = ('first', 'second', 'third', 'fourth', 'fifth', 'sixth', 'seventh', 'eighth', 'ninth', 'tenth', 'eleventh', 'twelfth')
    lines = ('twelve Drummers Drumming, ',
             'eleven Pipers Piping, ',
             'ten Lords-a-Leaping, ',
             'nine Ladies Dancing, ',
             'eight Maids-a-Milking, ',
             'seven Swans-a-Swimming, ',
             'six Geese-a-Laying, ',
             'five Gold Rings, ',
             'four Calling Birds, ',
             'three French Hens, ',
             'two Turtle Doves, and ',
             'a Partridge in a Pear Tree.')
    lyrics = []
    for i in range(start_verse,end_verse+1):
        verse = ''
        for j in range(1,i+1):
            verse  = lines[-j]+verse
        verse = 'On the '+numbers[i-1]+' day of Christmas my true love gave to me: '+verse   
        lyrics.append(verse)
    return lyrics