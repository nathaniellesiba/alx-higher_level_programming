#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """
    A class representing a square.

    Attributes:
        size (int): The length of each side of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a square with the given size.

        Args:
            size (int, optional): The length of each side of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
