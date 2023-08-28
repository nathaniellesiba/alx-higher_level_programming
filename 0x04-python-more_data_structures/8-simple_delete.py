#!/usr/bin/python3

"""The fixed code uses the del keyword to remove the specified key from"""
"""the a_dictionary. It then returns the modified dictionary.By using"""
"""the del keyword, we can directly delete the key-value pair from th"""
"""e dictionary without the need for additional steps."""
"""This ensures that the code is concise and efficient."""


def simple_delete(a_dictionary, key=""):
    del a_dictionary[key]
    return a_dictionary
