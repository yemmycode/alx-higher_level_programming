#!/usr/bin/python3
"""Defines a function for adding integers."""

def add_integer(a, b=98):
    """Return the integer addition of two numbers.

    Float arguments are converted to integers before addition.

    Args:
        a (int, float): First number.
        b (int, float, optional): Second number. Defaults to 98.

    Raises:
        TypeError: If either a or b is not an integer or float.
    
    Returns:
        int: Sum of the two numbers.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")
    return int(a) + int(b)
