#!/usr/bin/python3
"""
A module that defines a Base class
Rectangle class inherits from this.
"""
import json


class Base:
    """
    The `Base` class is the base class for managing unique
    IDs in future classes.

    Attributes:
        __nb_objects (int): A private class attribute that
        keeps track of the number of objects created.
        id (int): A public instance attribute representing the unique ID of an
        object.

    Methods:
        __init__(self, id=None):
            Constructor method for the `Base` class.

            Args:
                id (int, optional): An optional parameter representing the ID.
                If not provided, a unique ID will be assigned.

    Usage:
        base_instance = Base()  # Creates an instance with a unique ID.
        custom_base_instance = Base(100)  # Creates an instance with a
        specified ID (100).
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """
        Constructor method for the `Base` class.

        Args:
            id (int, optional): An optional parameter representing the ID.
            If not provided, a unique ID will be assigned.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """
        Static method that returns the JSON string representation of
        list_dictionaries.

        Args:
            list_dictionaries (list): A list of dictionaries to be
            converted to JSON.

        Returns:
            str: A JSON string representation of list_dictionaries.

        Example:
            data = [{'id': 1, 'name': 'Alice'}, {'id': 2, 'name': 'Bob'}]
            json_string = Base.to_json_string(data)
        """
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Save a list of objects to a JSON file.

        Args:
            cls (class): The class itself (automatically passed as the first
            argument).
            list_objs (list): A list of instances of a class that inherits
            from Base.

        Notes:
            - If list_objs is None, an empty list will be saved to the file.
            - The filename will be based on the class name, e.g.,
            "Rectangle.json" for a Rectangle class.

        Example:
            Rectangle.save_to_file([obj1, obj2])  # Saves obj1 and obj2 to
            "Rectangle.json".
        """
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        json_string = cls.to_json_string(
                     [obj.to_dictionary() for obj in list_objs])

        with open(filename, 'w') as file:
            file.write(json_string)

    @staticmethod
    def from_json_string(json_string):
        """
        Convert a JSON string representation into a list of dictionaries.

        Args:
            json_string (str): A JSON string representing a list of
            dictionaries.

        Returns:
            list: A list of dictionaries represented by the JSON string.

        Example:
            json_data = '[{"id": 1, "name": "Alice"}, {"id": 2,
            "name": "Bob"}]'
            data_list = Base.from_json_string(json_data)
        """
        if not json_string:
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """
        Create an instance with attributes set from a dictionary.

        Args:
            **dictionary: A dictionary containing attribute names and their
            values.

        Returns:
            object: An instance of the class with attributes set as specified
            in the dictionary.

        Example:
            data = {'width': 10, 'height': 20, 'x': 5, 'y': 5, 'id': 1}
            instance = Rectangle.create(**data)
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(5, 5)
        elif cls.__name__ == "Square":
            dummy = cls(5)
        else:
            return None

        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """
        Load a list of instances from a JSON file.

        Returns:
            list: A list of instances of the class loaded from the JSON file.

        Notes:
            - The filename is based on the class name, e.g., "Rectangle.json"
            for the Rectangle class.
            - If the file doesn't exist, an empty list is returned.
            - Instances are created using the create method and data from the
            file.

        Example:
            rectangle_instances = Rectangle.load_from_file()
        """
        filename = cls.__name__ + ".json"

        try:
            with open(filename, 'r') as file:
                json_data = file.read()
                instance_dict = cls.from_json_string(json_data)
                instances = [cls.create(**data) for data in instance_dict]
                return instances
        except FileNotFoundError:
            f("{filename} does not exist")
            return []
        except IOError:
            print("An error occurred while reading the file.")
            return []
