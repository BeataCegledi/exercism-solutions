
def square(number):
    """Return the number of grains on the given square of the chessboard."""
    if 0 < number < 65:
        return 2 ** (number - 1)
    raise ValueError("square must be between 1 and 64")


def total():
    """Return the total number of grains on the chessboard."""
    grains = 0
    for i in range(64):
        grains += 2 ** i
    return grains
