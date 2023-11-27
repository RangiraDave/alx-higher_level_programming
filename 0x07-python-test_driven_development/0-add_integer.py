#!/usr/bin/python3
"""
This function takes in two integers
or floats and returns integer sum.
"""


def add_integer(a, b=98):
    """
    Function to add two integers

    Args:
        a (int or float): First integer or float.
        b (int or float): Second integer or float. Defaults to 98.

    Returns:
        int: The addition of a and b.

    Raises:
        TypeError: If a or b is not an integer or float.
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    a = int(a)
    b = int(b)
    return a + b
