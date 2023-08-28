#!/usr/bin/python3

"""This code defines a function called multiply_by_2 that takes dictionary"""
"""a_dictionary as input. It uses a dictionary comprehension"""
"""to iterate over the key-value pairs in the input dictionary and"""
"""creates a new dictionary with the same keys but with the values"""
"""multiplied by 2. The resulting dictionary is then returned."""


def multiply_by_2(a_dictionary):
    return {key: value * 2 for key, value in a_dictionary.items()}
