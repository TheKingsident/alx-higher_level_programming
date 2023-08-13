#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    list_size = len(my_list)
    for i in range(1, (list_size + 1)):
        print("{:d}".format(my_list[list_size - i]))
