#!/usr/bin/python3

class TestClass:
    __slots__ = ['attr1']

obj = TestClass()
add_attribute(obj, 'attr1', 10)  # This will add the attribute 'attr1' to the object with the value 10
add_attribute(obj, 'attr2', 20)  # This will raise a TypeError with the message "can't add new attribute"

