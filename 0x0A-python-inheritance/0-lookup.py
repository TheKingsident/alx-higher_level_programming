#!/usr/bin/python3
"""
Retrieve a list of callable attributes (methods and functions) of an object.
"""


def lookup(obj):
    """
    Retrieve a list of callable attributes (methods and functions)
    of an object.

    Args:
        obj (object): The object for which to retrieve callable attributes.

    Returns:
        list: A list containing the names of callable attributes (methods
        and functions)
              belonging to the specified object.
    """
    o_dict = {}
    all_attributes = dir(obj)

    for attr in all_attributes:
        o_dict[attr] = getattr(obj, attr)

    return list(o_dict.keys())
