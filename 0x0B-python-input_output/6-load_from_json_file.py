#!/usr/bin/python3
"""
Defines a function
"""
import json


def load_from_json_file(filename):
    """
    Create a Python object from a JSON file.

    Parameters:
    filename (str): The name of the JSON file to read.

    Returns:
    any: A Python object represented by the JSON data in the file.

    Example:
    loaded_data = load_from_json_file("data.json")
    # This reads the content of "data.json" and returns the Python object
    represented by the JSON data.
    """
    with open(filename, "r") as f:
        return json.load(f)
