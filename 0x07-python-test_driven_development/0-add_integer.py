#!/usr/bin/python3

def add_integer(a, b=98):
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")

    return int(a) + int(b)

if __name__ == "__main__":
    import doctest
    doctest.testfile("tests/2-matrix_divided.txt")
