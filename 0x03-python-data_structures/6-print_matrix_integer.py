#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print()
        return

    for row_idx, row in enumerate(matrix):
        for column, element in enumerate(row):
            if column == len(row) - 1:
                if row_idx == len(matrix) - 1:
                    print("{:d}".format(element))
                else:
                    print("{:d}".format(element))
            else:
                print("{:d}".format(element), end=" ")
