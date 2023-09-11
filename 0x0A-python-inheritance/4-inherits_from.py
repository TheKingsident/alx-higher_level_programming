#!/usr/bin/python3
"""
Check if an object is an instance of a class that inherited
(directly or indirectly) from the specified class.
"""


def inherits_from(obj, a_class):
    """
    Check if an object is an instance of a class that inherited
    (directly or indirectly) from the specified class.

    Args:
        obj (object): The object to check.
        a_class (class): The class to compare against.

    Returns:
        bool: True if the object is an instance of the specified class,
        otherwise False.

    Example:
        class Parent:
            pass

        class Child(Parent):
            pass

        obj = Child()
        result = inherits_from(obj, Parent)
        print(result)  # Output: True

        other_obj = "Hello, World!"
        result = inherits_from(other_obj, Parent)
        print(result)  # Output: False
    """
    return issubclass(type(obj), a_class) and type(obj) is not a_class
