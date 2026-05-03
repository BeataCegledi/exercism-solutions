"""Converts a number to a string based on its divisibility.

Adds "Pling" if divisible by 3, "Plang" if divisible by 5,
and "Plong" if divisible by 7. If none apply, returns the
number as a string.
"""

def convert(number):
    sound = ""
    if number % 3 == 0:
        sound += "Pling"
    if number % 5 == 0:
        sound += "Plang"
    if number % 7 == 0:
        sound += "Plong"
    if sound == "":
        return str(number)
    return sound    