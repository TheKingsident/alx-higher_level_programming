#!/usr/bin/python3
"""
A module that defines a class representing a square, inheriting from
Rectangle.
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
    The `Square` class represents a square, which is a special case of a
    rectangle with equal width and height.

    Attributes:
        size (int): The size of the square, which is both the width and
        height.
        x (int): The x-coordinate of the top-left corner of the square.
        y (int): The y-coordinate of the top-left corner of the square.
        id (int): A public instance attribute representing the unique ID
        of the square.

    Methods:
        __init__(self, size, x=0, y=0, id=None):
            Constructor method for the `Square` class.

            Args:
                size (int): The size of the square, which is both the
                width and height.
                x (int, optional): The x-coordinate of the top-left corner
                of the square (default is 0).
                y (int, optional): The y-coordinate of the top-left corner
                of the square (default is 0).
                id (int, optional): An optional parameter representing the
                ID. If not provided, a unique ID will be assigned.

        __str__(self):
            String representation method that returns a formatted string
            describing the square.

        update(self, *args, **kwargs):
            Public method that assigns arguments to specific attributes,
            including key-worded arguments.

    Usage:
        square = Square(5)  # Creates a square with size 5 and default
        position and ID.
        custom_square = Square(10, 2, 3, 100)  # Creates a square with
        specified parameters and ID (100).
    """
    def __init__(self, size, x=0, y=0, id=None):
        """
        Constructor method for the `Square` class.

        Args:
            size (int): The size of the square, which is both the width
            and height.
            x (int, optional): The x-coordinate of the top-left corner of
            the square (default is 0).
            y (int, optional): The y-coordinate of the top-left corner of
            the square (default is 0).
            id (int, optional): An optional parameter representing the ID.
            If not provided, a unique ID will be assigned.
        """
        super().__init__(size, size, x, y, id)
        self.size = size

    def __str__(self):
        """
        String representation method that returns a formatted string
        describing the square.

        Example:
            square = Square(5)
            print(square)  # Output: "[Square] (1) 0/0 - 5"
        """
        return f"[Square] {(self.id)} {self.x}/{self.y} - {self.size}"

    @property
    def size(self):
        """
        Getter method for the size attribute.

        Returns:
            int: The size of the square, which is both the width and height.
        """
        return self.width

    @size.setter
    def size(self, size):
        """
        Setter method for the size attribute. Assigns the same value to
        width and height attributes.

        Args:
            size (int): The size of the square, which is both the width
            and height.
        """
        self.width = size
        self.height = size

    def update(self, *args, **kwargs):
        """
        Public method that assigns arguments to specific attributes,
        including key-worded arguments.

        Args:
            *args: Variable number of positional arguments (not used in
            this case).
            **kwargs: Keyword arguments where each key represents an
            attribute of the instance.

        Example:
            square = Square(5)
            square.update(100, size=10, x=2, y=3)
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.size = args[1]
            if len(args) >= 3:
                self.x = args[2]
            if len(args) >= 4:
                self.y = args[3]
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.size = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']

    def to_dictionary(self):
        """
        Public method that returns a dictionary representation of the Square
        instance.

        Returns:
            dict: A dictionary containing the following key-value pairs:
                - 'id': The unique ID of the square.
                - 'size': The size of the square.
                - 'x': The x-coordinate of the top-left corner of the
                square.
                - 'y': The y-coordinate of the top-left corner of the
                square.

        Example:
            square = Square(10, 20)
            dictionary = square.to_dictionary()
            # Output: {'id': 1, 'size': 10, 'x': 0, 'y': 0}
        """
        dim_dict = {
                    'id': self.id,
                    'size': self.size,
                    'x': self.x,
                    'y': self.y
                    }
        return dim_dict
