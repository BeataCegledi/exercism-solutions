"""Solve simple word-form math questions like 'What is 5 plus 3?'."""

OPERATIONS = ['What is ', ' plus ', ' minus ', ' multiplied by ', ' divided by ']


def operations(operation, result, value):
    """Apply one operation to the running result and return it."""
    if operation == 'What is ':
        return value
    if operation == ' plus ':
        return result + value
    if operation == ' minus ':
        return result - value
    if operation == ' multiplied by ':
        return result * value
    if operation == ' divided by ':
        if value == 0:
            raise ValueError('Divide by 0 is not possible')
        return result / value
    return result


def answer(question):
    """Parse a word-form math question and return the numeric result."""
    text = question.rstrip('?')
    end_result = 0
    while text:
        minus = False
        operation = next((op for op in OPERATIONS if text.startswith(op)), None)
        if operation is None:
            if any(op.strip() in text for op in OPERATIONS) or any(c.isdigit() for c in text):               
                raise ValueError('syntax error')
            raise ValueError('unknown operation')
        text = text[len(operation):]
        try:
            if text[0] == '-':
                text = text[1:]
                minus = True
            zahl = 0
            i = 0
            while i < len(text) and text[i].isdigit():
                zahl = zahl * 10 + int(text[i])
                i += 1
            text = text[i:]
            if minus:
                zahl = 0 - zahl
            end_result = operations(operation, end_result, zahl)
        except IndexError:
            raise ValueError('syntax error')
    return end_result