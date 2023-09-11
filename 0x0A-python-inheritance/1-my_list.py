#!/usr/bin/python3
"""
A module that defines a subclass
"""


class MyList(list):
    """
    The subclass
    """
    def print_sorted(self):
        """
        Prints the list in ascending sorted order.
        """
        sorted_list = sorted(self)
        print(sorted_list)
