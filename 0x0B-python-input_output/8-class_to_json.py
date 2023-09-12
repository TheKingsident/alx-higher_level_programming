#!/usr/bin/python3
"""
Defines a function
"""


def class_to_json(obj):
    """
    Convert an object to a dictionary suitable for JSON serialization.

    Parameters:
    obj (object): An instance of a class with serializable attributes.

    Returns:
    dict: A dictionary containing serializable attributes and their values.
    """
    a_dict = vars(obj)
    serializable = {
            key: value for key, value in a_dict.items()
            if isinstance(value, (list, dict, str, int, bool))
            }
    return serializable
