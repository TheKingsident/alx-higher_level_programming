#!/usr/bin/python3

"""
Print a square of '#' characters.
Args:
    size (int): The size of the square.
"""


def print_square(size):
    """
    Print a square of '#' characters.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        if i == 0 or i == size - 1:
            print('#' * size)
        else:
            print('#' + ' ' * (size - 2) + '#')
