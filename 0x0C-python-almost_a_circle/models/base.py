#!/usr/bin/python3

"""Import libraries for base model"""
from json import dumps, loads
import csv


class Base:

    """This is the base model, 
    it represent all classes in the project
    and doing so with provate class attribute
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """ this is initializing a new base
        """
        if id is not None:
            self.id = id  
            """ if id is not none, then
            assign the public instance attribute id with the argument value
            """
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

@staticmethod
def to_json_string(list_dictionaries):
    """a function that returns a json list of dictionaries

    args:
        the argument list_dictionaries is the list
    """
    If list_dictionaries is None or list_dictionaries == []:
        return "[]"
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
        if list_objs is not None:
            list_objs = [o.to_dictionary() for o in list_objs]
        with open("{}.json".format(cls.__name__), "w", encoding="utf-8") as f:
            f.write(cls.to_json_string(list_objs))


@staticmethod
def from_json_string(json_string):
    """return json string
    Args:
    json_string (str): a JSON str rep
    Return:
    json string as none
    """
    if json_string is None or json_string == "[]":
        return {}
    return json.loads(json_string)

@classmethod
def create(cls, **dictionary):
    """class pf disctionaries
    Args:
    ***dictionary (dict which pairs attribs to init
    """
    if dictionary and dictionary != {}:
        if cls.__name__ == "rectangle":
            new = cls (1, 1)
        else:
            new = cls(1)
            new.update(**dictionary)
        return new

def load_from_file(cls):
    """return list of instant classes from json strings
    reading from <cls.__name__>.json
    Returns:
    empty or initiated class
    """
    filename = str(cls.__name__) + ".json"
    try:
        with open(filename, "r") as jsonfile:
            list_dicts = Base.from_json_string(jsonfile.read())
            return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []

def save_to_file(cls. list_objs):
    """writes json serial list of objects to file
    Arg:
    list_obj(list) which inherit from Base instance
    """
      from models.rectangle import Rectangle
      from models.square import Square
      if list_objs is not None:
            if cls is Rectangle:
                list_objs = [[o.id, o.width, o.height, o.x, o.y]
                             for o in list_objs]
            else:
                list_objs = [[o.id, o.size, o.x, o.y]
                             for o in list_objs]
      with open('{}.csv'.format(cls.__name__), 'w', newline='',
                  encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(list_objs)


@classmethod
    def load_from_file_csv(cls):
        '''Loads object to csv file.'''
        from models.rectangle import Rectangle
        from models.square import Square
        ret = []
        with open('{}.csv'.format(cls.__name__), 'r', newline='',
                  encoding='utf-8') as f:
            reader = csv.reader(f)
            for row in reader:
                row = [int(r) for r in row]
                if cls is Rectangle:
                    d = {"id": row[0], "width": row[1], "height": row[2],
                         "x": row[3], "y": row[4]}
                else:
                    d = {"id": row[0], "size": row[1],
                         "x": row[2], "y": row[3]}
                ret.append(cls.create(**d))
        return ret

@staticmethod
    def draw(list_rectangles, list_squares):
        """draw the lines"""
        import turtle
        import time
        from random import randrange
        turtle.Screen().colormode(255)
        for i in list_rectangles + list_squares:
            t = turtle.Turtle()
            t.color((randrange(255), randrange(255), randrange(255)))
            t.pensize(1)
            t.penup()
            t.pendown()
            t.setpos((i.x + t.pos()[0], i.y - t.pos()[1]))
            t.pensize(10)
            t.forward(i.width)
            t.left(90)
            t.forward(i.height)
            t.left(90)
            t.forward(i.width)
            t.left(90)
            t.forward(i.height)
            t.left(90)
            t.end_fill()

        time.sleep(5)
