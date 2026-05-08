color_dict = {
    'black': 0, 'brown': 1, 'red': 2, 'orange': 3,
    'yellow': 4, 'green': 5, 'blue': 6,
    'violet': 7, 'grey': 8, 'white': 9
}

def label(colors):
    """Returns the resistance value of a resistor based on its first three color bands,     using the appropriate SI prefix."""
    result = (color_dict[colors[0]] * 10 + color_dict[colors[1]]) * (10 ** color_dict[colors[2]])

    if result == 0:
        return '0 ohms'
    if result % 1_000_000_000 == 0:
        return f'{result // 1_000_000_000} gigaohms'
    if result % 1_000_000 == 0:
        return f'{result // 1_000_000} megaohms'
    if result % 1_000 == 0:
        return f'{result // 1_000} kiloohms'
    return f'{result} ohms'
