#!/usr/bin/python3

def roman_to_int(roman_string):
    numerals = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
            }

    if roman_string is None or not roman_string:
        return 0

    integer, recent = 0, 0

    for character in reversed(roman_string):
        if numerals[character] >= recent:
            integer += numerals[character]
        else:
            integer -= numerals[character]
        recent = numerals[character]

    return integer
