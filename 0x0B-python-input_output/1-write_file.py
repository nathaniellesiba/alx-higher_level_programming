#!/usr/bin/python3
'''whatever method that calls module'''

def write_file(filename="", text=""):
    '''the prototype required'''
    with open(filename, 'w', encoding='utf-8') as file:
        num_chars_written = file.write(text)
    return num_chars_written
