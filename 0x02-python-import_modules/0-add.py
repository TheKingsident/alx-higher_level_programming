#!/usr/bin/python3

from add_0 import add as addition


def print_add():
    a = 1
    b = 2
    print(f"{a} + {b} = {addition(a, b)}")


print_add()
