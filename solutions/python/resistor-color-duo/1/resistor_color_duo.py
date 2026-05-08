
color_dict = {
    'black': 0, 'brown': 1, 'red': 2, 'orange': 3,
    'yellow': 4, 'green': 5, 'blue': 6,
    'violet': 7, 'grey': 8, 'white': 9
}


def value(colors):
    """
    Return the resistance value of a resistor based on its first two color bands.
    Extra colors are ignored.
    """
    
    return color_dict[colors[0]]*10 + color_dict[colors[1]]
