#!/usr/bin/python3
def transpose(matrix):
    """ Transpose a matrix """
    # Transpose the matrix by using list comprehension
    return [[row[i] for row in matrix] for i in range(len(matrix[0]))]


def dot_product(row_a, row_b):
    """ Multiply dot 2 matrix """
    # Use the built-in sum function and list comprehension to calculate the dot product
    return sum(a * b for a, b in zip(row_a, row_b))


def matrix_mul(m_a, m_b):
    """ Perform matrix multiplication """
    # Validate the input matrices as per the given requirements
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if not m_a or any(not row for row in m_a):
        raise ValueError("m_a can't be empty")
    if not m_b or any(not row for row in m_b):
        raise ValueError("m_b can't be empty")
    if any(not all(isinstance(item, (int, float)) for item in row) for row in m_a):
        raise TypeError("m_a should contain only integers or floats")
    if any(not all(isinstance(item, (int, float)) for item in row) for row in m_b):
        raise TypeError("m_b should contain only integers or floats")
    if len(set(len(row) for row in m_a)) != 1:
        raise TypeError("each row of m_a must be of the same size")
    if len(set(len(row) for row in m_b)) != 1:
        raise TypeError("each row of m_b must be of the same size")
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Transpose matrix m_b
    t_b = transpose(m_b)

    # Perform matrix multiplication using list comprehension
    result = [[dot_product(row_a, row_b) for row_b in t_b] for row_a in m_a]

    return result

