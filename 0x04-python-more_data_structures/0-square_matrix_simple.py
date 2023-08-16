#!/usr/bin/python3

"""function that computes square val of all int of matrix using ** opertr."""


def square_matrix_simple(matrix=[]):
    return [[num**2 for num in row] for row in matrix]
