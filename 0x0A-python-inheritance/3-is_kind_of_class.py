#!/usr/bin/python3
"""
Check if an object is an instance of, or if the object is an
instance of a class that inherited from, the specified class
"""


def is_kind_of_class(obj, a_class):
    """
    Check if an instance of, or if the object is an instance of a class that
    inherited from, the specified class

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
    if isinstance(obj, a_class):
        return True
    else:
        return False
