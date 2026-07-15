"""Find the sum of multiples in a range."""


def sum_of_multiples(limit, multiples):
    """Calculate sum of all multiples of given numbers below a limit.

    Args:
        limit: Upper bound (exclusive).
        multiples: List of base numbers.

    Returns:
        Sum of all multiples below the limit.
    """
    set_of_multi = set()
    for base in multiples:
        if base != 0:
            set_of_multi.update(multi for multi in range(base, limit, base))
    return sum(set_of_multi)