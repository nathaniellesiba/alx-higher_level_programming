#!/usr/bin/python3

class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.width = width
        self.height = height

# Creating an instance of Rectangle
r = Rectangle(5, 10)

# Calling the area method will raise an exception
r.area()  # This will raise an Exception with the message "area() is not implemented"

