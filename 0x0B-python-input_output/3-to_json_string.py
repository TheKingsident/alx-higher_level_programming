#!/usr/bin/python3
"""
Defines a function
"""
import json


def to_json_string(my_obj):
    """
    Convert a Python object to a JSON-formatted string.

    Parameters:
    my_obj (any): The Python object to be converted to JSON.

    Returns:
    str: A JSON-formatted string representing the input object.

    Example:
    my_dict = {"name": "John", "age": 30, "city": "New York"}
    json_string = to_json_string(my_dict)
    print(json_string)
    # Output: '{"name": "John", "age": 30, "city": "New York"}'
    """
    return json.dumps(my_obj)
