#!/usr/bin/python3

"""This code snippet defines a function print_sorted_dictionary that takes"""
"""a dictionary a_dictionary as input. It creates a list list_order"""
"""containing the keys of the dictionary using the keys() method."""
"""The list is then sorted in ascending order using the sort() method."""
"""Finally, a loop iterates over the sorted list and prints each key-value"""
"""pair in the format "key: value"."""


def print_sorted_dictionary(a_dictionary):
    list_order = list(a_dictionary.keys())
    list_order.sort()
    for key in list_order:
        print("{}: {}".format(key, a_dictionary[key]))
