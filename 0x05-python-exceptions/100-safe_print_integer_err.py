#!/usr/bin/python3

import sys


def safe_print_integer_err(value):
    message = "Unknown format code 'd' for object of type 'str'\n"

    try:
        print("{:d}".format(value), end="")

    except (TypeError, ValueError):
        sys.stderr.write("Exception: " + message)
        return False

    print()
    return True
