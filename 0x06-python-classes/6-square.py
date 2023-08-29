#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """
    A class representing a square
    """

    def __init__(self, size=0, position=(0, 0)):
        """
        Initializes a square with the given size and position.

        Args:
            size (int, optional): The length of the square
            position (tuple, optional): The position of the square"""
        self.size = size
        self.position = position

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
        Set the size of the square
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        Get the position of the square.

        Returns:
            tuple: The position of the square.
        """
        return (self.__position)

    @position.setter
    def position(self, value):
        """
        Set the position of the square.

        Args:
            value (tuple): The new position of the square.
        """
        if not (isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                any(i < 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """
        Calculate the area of the square
        """
        return (self.__size ** 2)

    def my_print(self):
        """
        Print a square pattern of '#' characters with the specified position.
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__position[1]):
                print()
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
