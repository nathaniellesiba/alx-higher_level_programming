#!/usr/bin/python3

"""The code defines a function square_matrix_map that takes a matrix as input. It uses the map function to iterate over each row in the matrix and apply the lambda function lambda x: x**2 to square each element in the row. The result is then converted back to a list using the list function. Finally, the outer map function is used to apply this operation to each row in the matrix, resulting in a new matrix with squared values.

By using the map function and lambda functions, we can achieve the desired result in a concise and efficient manner, without the need for explicit loops or imports."""

def square_matrix_map(matrix=[]):
    return list(map(lambda row: list(map(lambda x: x**2, row)), matrix))
