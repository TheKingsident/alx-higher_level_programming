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
    o_list = []
    all_attributes = dir(obj)

    o_list = [attr for attr in all_attributes if callable(getattr(obj, attr))]

    return o_list
