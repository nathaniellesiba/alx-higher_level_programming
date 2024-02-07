#!/usr/bin/python3
'''Module to lookup for the method'''

import json

def save_to_json_file(my_obj, filename):
    """
    Save an object to a text file using a JSON representation.

    Args:
    my_obj: The object to be serialized.
    filename: The name of the file to save the JSON representation to.

    Returns:
    None
    """
    with open(filename, 'w') as file:
        json.dump(my_obj, file)
