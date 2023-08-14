#!/usr/bin/python3

"""prints a matrix of integers"""
"""assume list only contains integers"""

def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        for num in i:
            print(''.join("{:d}".format(num)), end=" ")
        print()
