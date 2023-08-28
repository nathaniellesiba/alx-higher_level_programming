#!/usr/bin/python3

"""This code defines the best_score function that takes a dictionary"""
"""a_dictionary as input. It initializes max_key to None and max_value"""
"""to negative infinity. The function then iterates over each key-value"""
"""pair in the dictionary using the items() method. For each pair,"""
"""it compares the value with the current maximum value. If the value"""
"""is greater than the current maximum value, it updates max_key and"""
"""max_value with the current key and value. After iterating through"""
"""all the key-value pairs, the function"""
"""returns the key with the maximum value."""


def best_score(a_dictionary):
    max_key = None
    max_value = float('-inf')
    
    for key, value in a_dictionary.items():
        if value > max_value:
            max_key = key
            max_value = value
    
    return max_key
