#!/usr/bin/python3
"""Define a MagicClass"""


import math


class MagicClass:
    """Represent a circle.

    Attributes:
        __radius (float): The radius of the circle.
    """

    def __init__(self, radius=0):
        """Initialize a new MagicClass instance.

        Arg:
            radius (float or int): The radius of the new MagicClass.
        """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self.__radius = radius

    def area(self):
        """Calculate and return the area of the MagicClass."""
        return (self.__radius ** 2 * math.pi)

    def circumference(self):
        """Calculate and return The circumference of the MagicClass."""
        return (2 * math.pi * self.__radius)
