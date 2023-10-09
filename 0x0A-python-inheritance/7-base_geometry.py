#!/usr/bin/python3
"""
This module defines the base class for geometry-related operations.
"""


class BaseGeometry():
    """
    This is a base class for geometry-related operations.

    It serves as a foundation for other geometry classes by providing
    common attributes and methods.

    Example usage:
    class Rectangle(BaseGeometry):
        def __init__(self, width, height):
            self.width = width
            self.height = height

        def area(self):
            return self.width * self.height

    rect = Rectangle(5, 10)
    print(rect.area())  # Output: 50
    """

    def area(self):
        """
        Calculate the area of a geometric shape.

        This method should be implemented in derived classes.

        Raises:
            Exception: An Exception with the message "area() is not
            implemented."
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validate an integer value.

        Args:
            name (str): The name of the value being validated.
            value (int): The value to be validated.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
