#!/usr/bin/python3
"""
Define a function
"""


def write_file(filename="", text=""):
    """
    Write a string to a file. If the file doesn't exist, it will be created.

    Parameters:
    filename (str): The name of the file to write to or create.
    content (str): The string content to write to the file.

    Returns:
    char_written (int): Number of characters written
    """
    with open(filename, "w") as f:
        char_written = f.write(text)
    return char_written
