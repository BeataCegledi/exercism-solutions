"""Gigasecond exercise."""
from datetime import timedelta


def add(moment):
    """Return the date and time 1 gigasecond (10**9 seconds) after moment."""
    return moment + timedelta(seconds=1e9)
