"""Check whether brackets in a string are properly paired and nested."""

pairs = {'(': ')', '[': ']', '{': '}'}


def is_paired(input_string):
    """Return True if all brackets in the input are correctly paired and nested."""
    stack = []
    for char in input_string:
        if char in pairs:
            stack.append(char)
        elif char in pairs.values():
            if not stack or char != pairs[stack[-1]]:
                return False
            stack.pop()
    return not stack    