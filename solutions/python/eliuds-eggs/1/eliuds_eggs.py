"""Count eggs based on binary representation."""

def egg_count(display_value):
    """Return the number of 1-bits in the binary form of display_value."""
    eggs = display_value
    count = 0
    while eggs > 0:
        count += eggs % 2
        eggs = eggs // 2
    return count