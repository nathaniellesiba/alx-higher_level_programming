#!/usr/bin/python3

"""Enumerate() method adds a counter to an iterable and returns it in a form of enumerating object."""

def divisible_by_2(my_list=[]):
    bool = my_list[:]
    for count, i in enumerate(my_list):
        if i % 2 == 0:
            bool[count] = True
        else:
            bool[count] = False
    return bool
