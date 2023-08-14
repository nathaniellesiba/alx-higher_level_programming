#!/usr/bin/python3

"""prints a matrix of integers"""
"""assume list only contains integers"""
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for num in row:
"""The end=" " argument in the print() function ensures that each number is printed with a space separator. After printing all the numbers in a row, it moves to the next line using another print() statement"""
            print("{:d}".format(num), end=" ")
        print()
