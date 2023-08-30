#!/usr/bin/python3
"""Define a class Square."""


class Square:
    """
    A class representing a square.

    Attributes:
        __size (int): The length of each side of the square.
    """

    def __init__(self, size=0):
        """
        Initializes a square with the given size.

        Args:
            size (int): The length of each side of the square.
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
            value (int): The new length of each side of the square.

        Raises:
            TypeError: If the provided value is not an integer.
            ValueError: If the provided value is negative.
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

    def my_print(self):
        """
        Print the square with the # character
        """
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
