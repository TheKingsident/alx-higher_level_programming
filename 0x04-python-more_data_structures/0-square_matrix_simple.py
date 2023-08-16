#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    squared_matrix = tuple(map(lambda row: [values ** 2 for values in row],
                           matrix))
    return squared_matrix
