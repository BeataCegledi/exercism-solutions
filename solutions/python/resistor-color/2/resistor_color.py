
"""
Resistor Color Code helper.

This module provides utilities for working with resistor color bands.
It allows looking up the numeric value associated with a color and
listing all supported color bands according to the standard resistor
color code.
"""

color_dict = {'black' : 0, 'brown' : 1, 'red' : 2, 'orange' : 3, 'yellow' : 4, 'green' : 5, 'blue' : 6, 'violet': 7, 'grey' : 8, 'white' : 9}

def color_code(color):    
    """
    Return the numeric value associated with a given color band.
    """

    return color_dict[color]

def colors():   
    """
    Return a list of all supported resistor color bands.
    """

    return list(color_dict)