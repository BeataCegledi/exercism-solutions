def is_valid(isbn):
    """
    Validate an ISBN-10 identifier.

    An ISBN-10 consists of 10 characters. The first 9 must be digits.
    The last character may be a digit or 'X', where 'X' represents 10.
    Hyphens are allowed in the input but are ignored during validation.

    Args:
        isbn (str): The ISBN-10 string to validate.

    Returns:
        bool: True if the ISBN is valid, False otherwise.
    """

    
    isbn = isbn.replace("-", "")
    if len(isbn) != 10:
        return False
    check = 0
    for index in range(9):
        if not isbn[index].isdigit():
            return False
        check += int(isbn[index]) * (10-index)
    if isbn[9].upper() == 'X':
        check += 10
    elif isbn[9].isdigit():
        check += int(isbn[9])
    else:
        return False
    return check % 11 == 0
    