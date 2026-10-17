"""Evaluator for a small subset of Forth."""

class StackUnderflowError(Exception):
    """Raised when an operation needs more items than are on the stack."""

    def __init__(self, message="Insufficient number of items in stack"):
        super().__init__((message))
        self.message = message

stack = []
words = {}

def push(number):
    """Push a number onto the stack."""
    stack.append(number)


def addieren():
    """Pop the top two numbers and push their sum."""
    push(stack.pop()+stack.pop())


def multiplizieren():
    """Pop the top two numbers and push their product."""
    push(stack.pop()*stack.pop())


def subtrahieren():
    """Pop the top two numbers and push (second - top)."""
    push(stack.pop(-2)-stack.pop(-1))


def dividieren():
    """Pop the top two numbers and push (second // top).

    Raises:
        ZeroDivisionError: If the top of the stack is 0.
    """
    if stack[-1] == 0:
        raise ZeroDivisionError("divide by zero")
    push(stack.pop(-2)//stack.pop(-1))


def dup():
    """Duplicate the top of the stack."""
    push(stack[-1])


def drop():
    """Remove the top of the stack."""
    del stack[-1]


def swap():
    """Swap the top two items on the stack."""
    push(stack.pop(-2))


def over():
    """Copy the second item from the top onto the top."""
    push(stack[-2])


# Maps each built-in word to the function that implements it.
OPERATORS = {
    "DROP": drop, "DUP": dup,
    "+": addieren, "-": subtrahieren, "*": multiplizieren, "/": dividieren,
    "SWAP": swap, "OVER": over,
}
# Minimum number of stack items each built-in word needs to run.
STACK_MIN = {
    "DROP": 1, "DUP": 1,
    "+": 2, "-": 2, "*": 2, "/": 2,
    "SWAP": 2, "OVER": 2,
}


def operands(token):
    """Execute a single resolved token (number or built-in word).

    Raises:
        ValueError: If the token is not a number or a known word.
        StackUnderflowError: If the stack has too few items for the operation.
    """
    if token.isdigit():
        push(int(token))
    elif token.startswith("-") and token[1:].isdigit():
        push(-int(token[1:]))
    elif token not in words and token not in OPERATORS:
        raise ValueError("undefined operation")
    elif STACK_MIN[token] > len(stack):
        raise StackUnderflowError
    else:
        OPERATORS[token]()
    return stack


def evaluate(input_data):
    """Evaluate a sequence of Forth lines and return the resulting stack.

    Word definitions (": name ... ;") are expanded immediately, so a
    later redefinition never changes an already-defined word.

    Raises:
        ValueError: If a definition name is a number, or a token is undefined.
        StackUnderflowError: If an operation runs out of stack items.
    """
    global stack, words
    stack = []
    words = {}
    for data in input_data:
        if data.startswith(":") and data.endswith(";"):
            name, *oper = data[1:-1].upper().strip().split()
            if name.isdigit() or name.startswith("-") and name[1:].isdigit():
                raise ValueError("illegal operation")
            operands_list = []
            for _token in oper:
                if _token in words:
                    operands_list.extend(words[_token])
                else:
                    operands_list.append(_token)
            words[name] = operands_list
        else:
            for token in data.split():
                if token.upper() in words:
                    for sub_token in words[token.upper()]:
                        operands(sub_token)
                else:
                    operands(token.upper())
    return stack