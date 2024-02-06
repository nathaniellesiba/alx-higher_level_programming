#!/usr/bin/python3
'''Module to lookup for the method'''

def pascal_triangle(n):
    '''given prototype'''
    if n <= 0:
        return []

    triangle = [[1]]
    '''list with the first row of Pascal's triangle'''
    for i in range(1, n):
        row = [1]
        for j in range(1, i):
             row.append(triangle[i-1][j-1] + triangle[i-1][j])
        row.append(1)
        triangle.append(row)
        
    return triangle
