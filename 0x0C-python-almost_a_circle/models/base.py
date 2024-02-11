#!/usr/bin/python3

class Base:
    __nb_objects = 0  # private class attribute

    def __init__(self, id=None):
        if id is not None:
            self.id = id  # assign the public instance attribute id with the argument value
        else:
            Base.__nb_objects += 1  # increment __nb_objects
            self.id = Base.__nb_objects  # assign the new value to the public instance attribute id
