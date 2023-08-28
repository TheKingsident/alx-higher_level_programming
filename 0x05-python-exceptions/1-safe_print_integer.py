#!/usr/bin/python3

def safe_print_integer(value):

    try:
        print("{:d}".format(value), end="")
    except (TypeError, ValueError):
        return False
        pass

    print()
    return True
