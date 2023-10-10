#!/usr/bin/python3
"""
Defines a function
"""
import json


def save_to_json_file(my_obj, filename):
    """
    Serialize a Python object to JSON format and save it to a file.

    Parameters:
    my_obj (any): The Python object to be serialized to JSON.
    filename (str): The name of the file where the JSON data will be saved.

    Returns:
    None

    Example:
    my_dict = {"name": "John", "age": 30, "city": "New York"}
    save_to_json_file(my_dict, "output.json")
    # This will create or overwrite 'output.json' with the JSON
    representation of my_dict.
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
