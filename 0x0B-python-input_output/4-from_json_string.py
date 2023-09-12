#!/usr/bin/python3
"""
Defines a function
"""
import json


def from_json_string(my_str):
    """
    Convert a JSON-formatted string to a Python object.

    Parameters:
    json_string (str): The JSON-formatted string to be converted.

    Returns:
    any: A Python object representing the input JSON data.

    Example:
    json_string = '{"name": "John", "age": 30, "city": "New York"}'
    my_dict = from_json_string(json_string)
    print(my_dict)
    # Output: {'name': 'John', 'age': 30, 'city': 'New York'}
    """
    return json.loads(my_str)
