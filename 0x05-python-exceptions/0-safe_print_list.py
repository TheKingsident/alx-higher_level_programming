#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    items_printed = 0

    try:
        for i in range(x):
            print(my_list[i], end="")
            items_printed += 1

    except IndexError:
        pass

    print()
    return items_printed
