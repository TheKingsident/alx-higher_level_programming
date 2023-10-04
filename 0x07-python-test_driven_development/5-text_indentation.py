#!/usr/bin/python3

"""
prints a text with 2 new lines after each of these
characters: ., ? and :
Args:
    text (str): The text
"""


def text_indentation(text):
    """
    prints a text with 2 new lines after each of these
    characters: ., ? and :
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    line = ""
    for char in text:
        line += char
        if char in '.?:':
            print(line.strip(), end="\n\n")
            line = ""

    if line:
        print(line.strip(), end="")
