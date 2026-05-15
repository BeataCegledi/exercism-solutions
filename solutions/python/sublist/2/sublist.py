"""
This exercise stub and the test suite contain several enumerated constants.

Enumerated constants can be done with a NAME assigned to an arbitrary,
but unique value. An integer is traditionally used because it’s memory
efficient.
It is a common practice to export both constants and functions that work with
those constants (ex. the constants in the os, subprocess and re modules).

You can learn more here: https://en.wikipedia.org/wiki/Enumerated_type
"""

# Possible sublist categories.
# Change the values as you see fit.
SUBLIST = 'Sublist'
SUPERLIST = 'Superlist'
EQUAL = 'Equal'
UNEQUAL = 'Unequal'

def list_in_list(list_a, list_b):
    """Return True if list_a appears as a contiguous sub-sequence of list_b."""
    if not list_a:
        return True
    difference = len(list_b) - len(list_a)
    return any(list_b[slide:slide+len(list_a)] == list_a for slide in range(difference + 1))

    

def sublist(list_one, list_two):
    """Return EQUAL, SUBLIST, SUPERLIST or UNEQUAL describing how list_one relates to list_two."""
    if list_one == list_two:
        return EQUAL
    if list_in_list(list_one, list_two):
        return SUBLIST
    if list_in_list(list_two, list_one):
        return SUPERLIST
    return UNEQUAL