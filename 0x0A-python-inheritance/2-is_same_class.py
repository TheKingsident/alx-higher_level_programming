#!/usr/bin/python3
"""
Check if an object is exactly an instance of the specified class.
"""


def is_same_class(obj, a_class):
    """
    Check if an object is exactly an instance of the specified class.

    Args:
        obj (object): The object to check.
        a_class (class): The class to compare against.

    Returns:
        bool: True if the object is an instance of the specified class,
        otherwise False.

    Example:
        class MyClass:
            pass

        obj = MyClass()
        result = is_same_class(obj, MyClass)
        print(result)  # Output: True

        other_obj = "Hello, World!"
        result = is_same_class(other_obj, MyClass)
        print(result)  # Output: False
    """
    return type(obj) is a_class
