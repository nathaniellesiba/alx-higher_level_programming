#!/usr/bin/python3
'''module to lookup for the method'''

def append_write(filename="", text=""):
    '''give prototype to use'''

    with open(filename, 'a', encoding='utf-8') as file:
        file.write(text)
    return len(text)
