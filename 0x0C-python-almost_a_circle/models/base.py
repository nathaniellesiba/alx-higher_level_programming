#!/usr/bin/python3

"""Import libraries for base model"""
#import json
#import csv
#import turtle


class Base:

    """This is the base model, 
    it represent all classes in the project
    and doing so with provate class attribute
    """
    __nb_objects = 0  # private class attribute

    def __init__(self, id=None):
        """ this is initializing a new base
        """
        if id is not None:
            self.id = id  
            """ if id is not none, then
            assign the public instance attribute id with the argument value
            """
        else:
            Base.__nb_objects += 1  # increment __nb_objects
            self.id = Base.__nb_objects  # assign the new value to the public instance attribute id
