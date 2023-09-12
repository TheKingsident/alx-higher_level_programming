#!/usr/bin/python3
"""
Defines a function
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Insert a line of text after each line containing a
    specific string in a file.

    Parameters:
    filename (str): The name of the file to modify.
    search_string (str): The string to search for in each line.
    new_string (str): The line of text to insert after lines
    containing the search string.

    Returns:
    None
    """
    with open(filename, "r") as file:
        lines = file.readlines()

    with open(filename, "w") as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string + "\n")
