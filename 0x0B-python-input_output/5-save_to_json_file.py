#!/usr/bin/python3
'''Module to lookup for the method'''

import json

def save_to_json_file(my_obj, filename):
    '''the prototype required'''
    with open(filename, 'w') as file:
        json.dumb(my_obj, file)