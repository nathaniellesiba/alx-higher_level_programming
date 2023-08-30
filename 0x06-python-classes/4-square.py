#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """
    A class representing a square.
    """

    def __init__(self, size=0):
        """
        Initializes a square with the given size.

        Args:
            size (int, optional): The length of each side of the square
        """
        self.size = size

    @property
    def size(self):
        """
        Get the size of the square.

        Returns:
            int: The length of each side of the square.
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """
        Set the size of the square.

        Args:
            value (int): The new length of each side of the square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        Calculate the area of the square.

        Returns:
            int: The area of the square.
        """
        return (self.__size * self.__size)
