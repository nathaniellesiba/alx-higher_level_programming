#!/usr/bin/python3
'''whatever method that calls module'''

def write_file(filename="", text=""):
    '''the prototype required'''
    with open(filename, 'w', encoding='utf-8') as file:
        f.write('this is a sample\n')
