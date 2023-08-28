#!/usr/bin/python3

"""The code defines a function called only_diff_elements that takes two"""
"""sets, set_1 and set_2, as input. The symmetric_difference method is"""
"""used to find the elements that are present in only one of the sets."""
"""The result is returned as a new set"""


def only_diff_elements(set_1, set_2):
    return set_1.symmetric_difference(set_2)
