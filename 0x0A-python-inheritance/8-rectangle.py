#!/usr/bin/python3
"""
A module that defines a class representing a rectangle, inheriting from
BaseGeometry.
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    A class representing a rectangle, inheriting from BaseGeometry.

    Attributes:
        __width (int): The width of the rectangle.
        __height (int): The height of the rectangle.

    Methods:
        __init__(self, width, height):
            Initializes a Rectangle instance with the given width and height.
            The width and height must be positive integers, validated by
            integer_validator.

    Usage:
        # Creating a Rectangle instance with a width of 5 and height of 10
        rectangle = Rectangle(5, 10)
    """
    def __init__(self, width, height):
        """
        Initializes a Rectangle instance with the given width and height.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.

        Raises:
            TypeError: If width or height is not a positive integer.

        Example:
            # Creating a Rectangle instance
            rectangle = Rectangle(5, 10)
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", self.__width)
        self.integer_validator("height", self.__height)
