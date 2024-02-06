#!/usr/bin/python3
'''method that calls the module'''

def read_file(filename=""):
    '''prototype for read_file and its file name'''
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')
