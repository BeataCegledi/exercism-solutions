"""
Functions to compute square of sum, sum of squares,
and their difference for a given number.
"""


def square_of_sum(number):
    """Return the square of the sum of numbers from 1 to number."""
    return sum(range(number + 1)) ** 2


def sum_of_squares(number):
    """Return the sum of squares of numbers from 1 to number."""
    return sum(item ** 2 for item in range(number + 1))


def difference_of_squares(number):
    """Return the difference between square_of_sum and sum_of_squares."""
    return abs(square_of_sum(number) - sum_of_squares(number))  