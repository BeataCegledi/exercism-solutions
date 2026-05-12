"""List operations implemented from scratch.

Functional-style implementations of classic list operations:
append, concat, filter, length, map, foldl, foldr, reverse.
Python built-ins (sum, reversed, slicing, list comprehensions) are used
only as building blocks; the higher-level operations are written by hand.
"""


def append(list1, list2):
    """Concatenate two lists into a new list."""
    return list1 + list2 


def concat(lists):
    """Flatten a list of lists into a single list."""
    result = []
    for item in lists:
        result.extend(item)
    return result

def filter(function, list):
    """Return the items for which the predicate is true."""
    return [item for item in list if function(item)]


def length(list):
    """Return the number of items in the list (without using len())."""
    return sum(1 for _ in list)
    
def map(function, list):
    """Apply the function to every item and return a new list."""
    return [function(item) for item in list]


def foldl(function, list, initial):
    """Reduce the list into the accumulator from the left."""
    for item in list:
        initial = function(initial, item)
    return initial

def foldr(function, list, initial):
    """Reduce the list into the accumulator from the right."""
    for item in reversed(list):
        initial = function(initial, item)
    return initial

def reverse(list):
    """Return a new list with the items in reverse order."""
    return list[::-1]