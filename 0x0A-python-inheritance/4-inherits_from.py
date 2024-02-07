#!/usr/bin/python3
'''Module to lookup for the method'''

def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited (directly or indirectly) from the specified class; otherwise False.

    Args:
    obj: The object to be checked.
    a_class: The specified class to compare against.

    Returns:
    True if obj is an instance of a class that inherited (directly or indirectly) from a_class; otherwise False.
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class

class ParentClass:
    pass

class ChildClass(ParentClass):
    pass

obj1 = ChildClass()
obj2 = "Hello"
print(inherits_from(obj1, ParentClass))  # This will return True
print(inherits_from(obj1, object))  # This will return True
print(inherits_from(obj2, int))  # This will return False

