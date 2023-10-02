#!/usr/bin/python3
"""
Adds two integers or floats and returns the result as a integer.
- Two numeric arguments, 'a' and 'b', which can be either integers or floats.
- It raises a TypeError if either 'a' or 'b' is not a numeric type.
"""


def add_integer(a, b=98):
    """
    Adds two integers or floats and returns the result as an integer.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
