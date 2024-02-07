#!/usr/bin/python3
'''Module to lookup for the method'''

def is_kind_of_class(obj, a_class):
    """
    Returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class; otherwise False.

    Args:
    obj: The object to be checked.
    a_class: The specified class to compare against.

    Returns:
    True if obj is an instance of, or if the object is an instance of a class that inherited from, a_class; otherwise False.
    """
    return isinstance(obj, a_class)

class ParentClass:
    pass

class ChildClass(ParentClass):
    pass

obj1 = ChildClass()
obj2 = "Hello"
print(is_kind_of_class(obj1, ParentClass))  # This will return True
print(is_kind_of_class(obj1, object))  # This will return True
print(is_kind_of_class(obj2, int))  # This will return False
