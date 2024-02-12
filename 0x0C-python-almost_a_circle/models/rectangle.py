#!/usr/bin/python3
"""models for rectangle"""
from models.base import Base

class Rectangle(Base):
    """this is the rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """the initialize of width, height, x and y dimensions"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        self.validate_integer("width", value, False)
        self.__width = value

    @property
    def height(self):
        """height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        self.validate_integer("height", value, False)
        self.__height = value

    @property
    def x(self):
        """x position of the rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        self.validate_integer("x", value, False)
        self.__x = value

    @property
    def y(self):
        """y position of the triangle"""
        return self.__y

    @y.setter
    def y(self, value):
        self.validate_integer("y", value, False)
        self.__y = value

    def area(self):
        return self.__width * self.__height
