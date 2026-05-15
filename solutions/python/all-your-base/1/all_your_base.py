"""Convert digits from input_base to output_base."""
def rebase(input_base, digits, output_base):
    """
    Convert a number represented as a list of digits from one base to another.
    
    Args:
        input_base (int): The base of the input number (>= 2).
        digits (list[int]): The digits of the number in input_base.
        output_base (int): The base to convert to (>= 2).

    Returns:
        list[int]: The digits of the converted number in output_base.

    Raises:
        ValueError: If bases are invalid or digits are out of range.
    """

    if input_base < 2:
        raise ValueError("input base must be >= 2")
    if not all(0 <= number < input_base for number in digits): 
        raise ValueError("all digits must satisfy 0 <= d < input base")
    if output_base < 2:
        raise ValueError("output base must be >= 2")
    if not digits:
        return [0]
    value = 0
    for index, digit in enumerate(reversed(digits)):
        value += digit * (input_base ** index)
    if value == 0:
        return [0]
    result = []
    while value > 0:
        result.append(value % output_base)
        value = value // output_base
    return result[::-1]
        
