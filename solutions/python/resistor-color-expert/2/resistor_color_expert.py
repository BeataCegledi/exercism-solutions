tolerance_dict = {
    'grey' : ' ±0.05%', 'violet' : ' ±0.1%', 'blue' : ' ±0.25%', 
    'green' : ' ±0.5%', 'brown' : ' ±1%', 'red' : ' ±2%', 
    'gold' : ' ±5%', 'silver' : ' ±10%'}

color_dict = {
    'black': 0, 'brown': 1, 'red': 2, 'orange': 3,
    'yellow': 4, 'green': 5, 'blue': 6,
    'violet': 7, 'grey': 8, 'white': 9}

def resistor_label(colors):

    """Return the resistance label for a resistor given its color bands.

    Accepts 1, 4, or 5 color bands. Formats the resistance value using
    the appropriate SI prefix (kilo-, mega-, giga-) and appends the
    tolerance from the last band (4- and 5-band resistors only).

    :param colors: list of color name strings, e.g. ['red', 'black', 'brown', 'gold']
    :return: formatted resistance string, e.g. '200 ohms ±5%'
    """

    if len(colors) == 1:
        return f'{color_dict[colors[0]]} ohms'
    tolerance = tolerance_dict[colors[-1]]        
    if len(colors) == 4:    
        result = (color_dict[colors[0]] * 10 + color_dict[colors[1]]) * (10 ** color_dict[colors[2]])
    else:
        result = (color_dict[colors[0]] * 100 + color_dict[colors[1]] * 10 + color_dict[colors[2]]) * (10 ** color_dict[colors[3]])

    if result == 0:
        return '0 ohms'
    if result >= 1_000_000_000:
        return f'{result / 1_000_000_000:g} gigaohms{tolerance}'
    if result >= 1_000_000:
        return f'{result / 1_000_000:g} megaohms{tolerance}'
    if result >= 1_000:
        return f'{result / 1_000:g} kiloohms{tolerance}'
    return f'{result} ohms{tolerance}'