#!/usr/bin/python3
"""
A module that defines a class representing a square, inheriting from
Rectangle.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    A class representing a square, inheriting from Rectangle.

    Attributes:
        __width (int): The width of the square.
        __height (int): The height of the square.

    Methods:
        __init__(self, size):
            Initializes a Square instance with the given width and height.
            The width and height must be positive integers, validated by
            integer_validator.

    Usage:
        # Creating a Square instance with a width of 5 and height of 10
        square = Square(5, 10)
    """

    def __init__(self, size):
        """
        Initializes a square instance with the given width and height.

        Args:
            size (int): The width of the square.

        Raises:
            TypeError: size is not a positive integer.

        Example:
            # Creating a Square instance
            square = Square(10)
        """
        super().__init__(size, size)
        self.__size = size
        self.__width = size
        self.__height = size
        self.integer_validator("size", size)

    def area(self):
        """
        Computes and returns the area of the square.

        Returns:
            int: The area of the square.
        """
        return self.__size * self.__size

    def __str__(self):
        return "[Square] {}/{}".format(self.__width, self.__height)
