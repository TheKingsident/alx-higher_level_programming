#!/usr/bin/python3
"""
Defines a function that open a file
"""


def read_file(filename=""):
    """
    Reads and prints the content of a text file line by line.

    Parameters:
    filename (str): The name of the file to be read.

    Returns:
    None
    """
    with open(filename, "r") as f:
        for line in f:
            print(line, end='')
