#!/usr/bin/python3
'''Module to call MyList'''

class MyList(list):
    '''custom function MyList'''
    def print_sorted(self):
        '''method for printing sorted list'''
        sorted_list = sorted(self)
        print(sorted_list)
