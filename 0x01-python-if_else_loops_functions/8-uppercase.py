#!/usr/bin/python3

def uppercase(s):
    statement = ""
    for character in s:
        if 'a' <= character <= 'z':
            statement += "{}".format(chr(ord(character) - ord('a') + ord('A')))
        else:
            statement += "{}".format(character)
    print(statement)
