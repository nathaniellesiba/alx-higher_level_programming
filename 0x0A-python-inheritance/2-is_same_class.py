#!/usr/bin/python3
'''Module to lookup for the method'''

def is_same_class(obj, a_class):
    """
    Returns True if the object is exactly an instance of the specified class; otherwise False.

    Args:
    obj: The object to be checked.
    a_class: The specified class to compare against.

    Returns:
    True if obj is exactly an instance of a_class; otherwise False.
    """
    return type(obj) is a_class
