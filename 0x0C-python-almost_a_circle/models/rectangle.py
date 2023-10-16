#!/usr/bin/python3

from models.base import Base


class Rectangle(Base):
    """
    The `Rectangle` class represents rectangles with width, height,
    position (x, y), and a unique ID.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int): The x-coordinate of the top-left corner of the rectangle.
        y (int): The y-coordinate of the top-left corner of the rectangle.
        id (int): A public instance attribute representing the unique ID of
        the rectangle.

    Methods:
        __init__(self, width, height, x=0, y=0, id=None):
            Constructor method for the `Rectangle` class.

            Args:
                width (int): The width of the rectangle.
                height (int): The height of the rectangle.
                x (int, optional): The x-coordinate of the top-left corner
                of the rectangle (default is 0).
                y (int, optional): The y-coordinate of the top-left corner
                of the rectangle (default is 0).
                id (int, optional): An optional parameter representing the
                ID. If not provided, a unique ID will be assigned.

    Usage:
        rectangle = Rectangle(10, 20)  # Creates a rectangle with width 10,
        height 20, and default position and ID.
        custom_rectangle = Rectangle(30, 40, 5, 5, 100)  # Creates a
        rectangle with specified parameters and ID (100).
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Constructor method for the `Rectangle` class.

        Args:
            width (int): The width of the rectangle.
            height (int): The height of the rectangle.
            x (int, optional): The x-coordinate of the top-left corner of the
            rectangle (default is 0).
            y (int, optional): The y-coordinate of the top-left corner of the
            rectangle (default is 0).
            id (int, optional): An optional parameter representing the ID.
            If not provided, a unique ID will be assigned.
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """
        Getter method for the width property of the rectangle.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Setter method for the width property of the rectangle with validation.

        Args:
            value (int): The new width value to set.

        Raises:
            TypeError: If the value is not an integer.
            ValueError: If the value is less than or equal to 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """
        Public method that calculates and returns the area of the Rectangle
        instance.

        Returns:
            int: The area of the rectangle (width * height).
        """
        return self.__width * self.__height

    def display(self):
        """
        Public method that prints the Rectangle instance using '#' characters.

        Example:
            For a rectangle with width 3 and height 2, the output would be:
            ###
            ###
        """
        for _ in range(self.__y):
            print()
        for _ in range(self.__height):
            print(" " * self.__x + "#" * self.__width)

    def __str__(self):
        """
        Overrides the default string representation to return a formatted
        string.

        Returns:
            str: A formatted string representing the Rectangle instance.
        """
        return (
            f"[Rectangle] ({self.id}) {self.x}/{self.y} - "
            f"{self.width}/{self.height}"
        )

    def update(self, *args, **kwargs):
        """
        Public method that assigns arguments to specific attributes,
        including key-worded arguments.

        Args:
            *args: Variable number of positional arguments (not used in this
            case).
            **kwargs: Keyword arguments where each key represents an attribute
            of the instance.

        Example:
            rectangle = Rectangle(10, 20)
            rectangle.update(100, width=30, height=40, x=5, y=5)
        """
        if args:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) >= 2:
                self.width = args[1]
            if len(args) >= 3:
                self.height = args[2]
            if len(args) >= 4:
                self.x = args[3]
            if len(args) >= 5:
                self.y = args[4]
        else:
            if 'width' in kwargs:
                self.width = kwargs['width']
            if 'height' in kwargs:
                self.height = kwargs['height']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']
            if 'id' in kwargs:
                self.id = kwargs['id']

    def to_dictionary(self):
        """
        Public method that returns a dictionary representation of the Rectangle
        instance.

        Returns:
            dict: A dictionary containing the following key-value pairs:
                - 'id': The unique ID of the rectangle.
                - 'width': The width of the rectangle.
                - 'height': The height of the rectangle.
                - 'x': The x-coordinate of the top-left corner of the
                rectangle.
                - 'y': The y-coordinate of the top-left corner of the
                rectangle.

        Example:
            rectangle = Rectangle(10, 20)
            dictionary = rectangle.to_dictionary()
            # Output: {'id': 1, 'width': 10, 'height': 20, 'x': 0, 'y': 0}
        """
        dim_dict = {
                    'id': self.id,
                    'width': self.width,
                    'height': self.height,
                    'x': self.x,
                    'y': self.y
                    }
        return dim_dict
