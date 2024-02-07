#!/usr/bin/python3
'''Module to lookup for the method'''


import json

def load_from_json_file(filename):
    """
    Load an object from a JSON file.

    Args:
    filename: The name of the JSON file to load the object from.

    Returns:
    The object loaded from the JSON file.
    """
    with open(filename, 'r') as file:
        return json.load(file)
