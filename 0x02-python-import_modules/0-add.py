#!/usr/bin/python3

from add_0 import add as addition


def print_add():
    a = 1
    b = 2
    print("{}".format(a), "+ {}".format(b), "= {}".format(addition(a, b)))


if __name__ == "__main__":
    print_add()
