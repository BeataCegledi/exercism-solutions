def line_up(name, number):
    """Return a personalized thank-you message with the ordinal number of the customer."""
    
    if number % 100 != 11 and number % 10 == 1:
        suffix = 'st'
    elif number % 100 != 12 and number % 10 == 2:
        suffix = 'nd'
    elif number % 100 != 13 and number % 10 == 3:
        suffix = 'rd'
    else:
        suffix = 'th'
    return f'{name}, you are the {number}{suffix} customer we serve today. Thank you!'
