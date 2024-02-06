#!/usr/bin/python3
'''Module to lookup for the method'''

def append_after(filename="", search_string="", new_string=""):
    '''the prototype given'''
    with open(filename, 'r+') as file:
        lines = file.readlines()
        file.seek(0)
        '''to start writing from the beginning'''

        for line in lines:
            '''storing in lines variable'''
            file.write(line)
            if search_string in line:
                file.write(new_string + '\n')
        file.truncate()
