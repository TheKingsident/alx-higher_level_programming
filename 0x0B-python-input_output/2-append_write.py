#!/usr/bin/python3
"""
Defines a function
"""


def append_write(filename="", text=""):
    """
    Appends a string to a file. If the file doesn't exist, it will be created.

    Parameters:
    filename (str): The name of the file to write to or create.
    content (str): The string content to write to the file.

    Returns:
    Number of characters written
    """
    with open(filename, "a") as f:
        return f.write(text)
