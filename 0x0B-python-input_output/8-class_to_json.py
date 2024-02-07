#!/usr/bin/python3
'''Module to lookup for the method'''

def class_to_json(obj):
    """
    Return the dictionary description with a simple data structure for JSON serialization of an object.

    Args:
    obj: An instance of a Class with serializable attributes: list, dictionary, string, integer, and boolean.

    Returns:
    A dictionary containing the serializable attributes of the object.
    """
    # Get all attributes of the object
    attributes = obj.__dict__

    # Construct a dictionary with serializable attributes
    serializable_dict = {}
    for key, value in attributes.items():
        if isinstance(value, (list, dict, str, int, bool)):
            serializable_dict[key] = value

    return serializable_dict

