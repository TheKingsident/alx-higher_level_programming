#!/usr/bin/python3

"""
This module contains the class Square.
"""


class Square:
    """
    Represents a square shape.

    This class defines a square with a size private attribute.
    """

    def __init__(self, size=0):
        """
        Initializes a new instance of Square.

        Args:
            size (int): The size of the square (default is 0).

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size is less than 0.
        """
        self.size = size  # Use the property setter

    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (int): The new size value.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculates the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    def my_print(self):
        """
        Prints the square.

        # respresents a square unit
        """
        if self.size == 0:
            print()
            return

        for _ in range(self.size):
            print("#" * self.size)
