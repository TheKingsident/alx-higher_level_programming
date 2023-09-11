#!/usr/bin/python3
"""
This module contains a class MyInt that inherits from int
"""


class MyInt(int):
    def __eq__(self, other):
        """
        Overrides the equality operator (==) to invert its behavior.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Overrides the inequality operator (!=) to invert its behavior.
        """
        return super().__eq__(other)
