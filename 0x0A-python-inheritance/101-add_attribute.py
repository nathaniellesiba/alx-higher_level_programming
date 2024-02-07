#!/usr/bin/python3
'''Module to lookup for the method'''

def add_attribute(obj, attr, value):
    """
    Adds a new attribute to an object if it's possible.

    Args:
    obj: The object to which the new attribute should be added.
    attr: The name of the new attribute.
    value: The value of the new attribute.

    Raises:
    TypeError: If the object can't have a new attribute, it raises a TypeError with the message "can't add new attribute".
    """
    if hasattr(obj, "__dict__") or (hasattr(type(obj), "__slots__") and attr in type(obj).__slots__):
        setattr(obj, attr, value)
    else:
        raise TypeError("can't add new attribute")

class TestClass:
    __slots__ = ['attr1']

obj = TestClass()
add_attribute(obj, 'attr1', 10)  # This will add the attribute 'attr1' to the object with the value 10
add_attribute(obj, 'attr2', 20)  # This will raise a TypeError with the message "can't add new attribute"
