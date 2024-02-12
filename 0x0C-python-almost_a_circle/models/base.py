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

@staticmethod
"""method that is being added
"""
def to_json_string(list_dictionaries):
    """a function that returns a json list of dictionaries
    and the argument list_dictionaries is the list
    """
    If list_dictionaries is None or list_dictionaries == []:
        return "[]"
    """return empty for none
    """
    return json.dumps(list_dictionaries)

@classmethod
"""method that is being added
"""
def save_to_file(cls, list_objs):
    """writing a JSON serial list for objects
    writing them to a file with arguments named list_obj(list)
    """
    filename = cls.__name__ + ".json"
    """this is the name of the file starting with cls for class"""
    with open(filename, "w") as jsonfile:
        if list_objs is None:
            jsonfile.write("[]")
        else:
            list_dicts = [o.to_disctionary() for o in list_objs]
            jsonfile.write(Base.to_json_string(list_dicts))
