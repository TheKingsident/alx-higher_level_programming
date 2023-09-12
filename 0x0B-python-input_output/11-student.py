#!/usr/bin/python3
"""
Defines a class
"""


class Student:
    """
    Represents a student with first_name, last_name, and age attributes.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initialize a Student instance with first_name, last_name, and age.

        Parameters:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of a Student instance.

        Returns:
        dict: A dictionary containing the student's attributes.
        """
        if attrs is None:
            return {
                "first_name": self.first_name,
                "last_name": self.last_name,
                "age": self.age
            }
        else:
            return {
                attr: getattr(self, attr)
                for attr in attrs
                if hasattr(self, attr) and type(
                        getattr(self, attr)) in (str, int, bool)
            }

    def reload_from_json(self, json_data):
        """
        Replace all attributes of the Student instance based on a JSON dictionary.

        Parameters:
        json_data (dict): A dictionary containing attribute names and their values.

        Returns:
        None
        """
        for attr, value in json_data.items():
            setattr(self, attr, value)
