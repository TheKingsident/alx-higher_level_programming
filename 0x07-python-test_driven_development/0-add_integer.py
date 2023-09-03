#!/usr/bin/python3

def add_integer(a, b=98):
    """
    Adds two integers or floats and returns the result as an integer.

    Args:
        a (int or float): The first number to be added.
        b (int or float, optional): The second number to be added. Default is 98.

    Returns:
        int: The sum of 'a' and 'b' as an integer.

    Raises:
        TypeError: If 'a' or 'b' is not an integer or float.
        
    Notes:
    - This function takes two numeric arguments, 'a' and 'b', which can be either integers or floats.
    - It raises a TypeError if either 'a' or 'b' is not a numeric type.
    - The function converts 'a' and 'b' to integers if they are initially provided as floats.
    - The result of the addition is always returned as an integer, even if 'a' and 'b' were initially floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return a + b
