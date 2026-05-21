'''Functions for creating an acronym from a phrase'''

import string

def abbreviate(words):
    '''Return an uppercase acronym from a phrase.

    :param words: str - a phrase containing words separated by spaces and/or hyphens.
    :return: str - the acronym formed from the first letter of each word, uppercased.'''
    
    clean = words.replace('-', ' ').translate(str.maketrans('', '', string.punctuation))
    return ''.join(word[0].upper() for word in clean.split())
    