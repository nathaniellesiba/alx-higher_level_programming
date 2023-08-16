#!/usr/bin/python3

"""function that computes square value of all int of a matrix using ** operator."""

def square_matrix_simple(matrix=[]):
    return [[num**2 for num in row] for row in matrix]
