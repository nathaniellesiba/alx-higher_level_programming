#!/usr/bin/python3
"""models for rectangle"""
from models.base import Base

class Rectangle(Base):
    def __init__(self, id=None, width, height, x=0, y=0):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Width of the rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        self.validate_integer("width", value, False)
        self.__width = value

    @property
    def height(self):
        """Height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        self.validate_integer("height", value, False)
        self.__height = value

    @property
    def x(self):
        """X-coordinate of the rectangle"""
        return self.__x

    @x.setter
    def x(self, value):
        self.validate_integer("x", value)
        self.__x = value

    @property
    def y(self):
        """Y-coordinate of the rectangle"""
        return self.__y

    @y.setter
    def y(self, value):
        self.validate_integer("y", value)
        self.__y = value

    def validate_integer(self, name, value, eq=True):
        """Method for validation"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if eq and value < 0:
            raise ValueError("{} must be >= 0".format(name))
        elif not eq and value <= 0:
            raise ValueError("{} must be > 0".format(name))

def area(self):
    """area of rectangle computed"""
    return self.with * self.height

def display(self):
        '''Prints string representing this rectangle.'''
        s = '\n' * self.y + \
            ('\n'.join([' ' * self.x + '#' * self.width for _ in range(self.height)]) + '\n')
        print(s, end='')



def __str__(self):
    """return string info about rectangle"""
     return '[{}] ({}) {}/{} - {}/{}'.format(type(self).__name__, id(self), self.x, self.y, self.width, self.height)

def __update(self, id=None, width=None, height=None, x=None, y=None):
        '''Internal method that updates instance attributes via */**args.'''
        if id is not None:
            self.id = id
        if width is not None:
            self.width = width
        if height is not None:
            self.height = height
        if x is not None:
            self.x = x
        if y is not None:
            self.y = y

def update(self, *args, **kwargs):
        '''Updates instance attributes via no-keyword & keyword args.'''
        if args:
            self.__update(*args)
        elif kwargs:
            self.__update(**kwargs)

def to_dictionary(self):
        '''Returns dictionary representation of this class.'''
        return {"id": self.id, "width": self.width, "height": self.height,
                "x": self.x, "y": self.y}
