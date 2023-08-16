#!/usr/bin/python3

"""This function takes 3 args[a_dictionary: The dictionary that needs to be updated. key: The key that needs to be updated or added. value: The value that needs to be assigned to the key. The function first checks if the key already exists in the dictionary. If it does, the value associated with the key is replaced with the new value. If the key doesn't exist, a new key-value pair is added to the dictionary."""

def update_dictionary(a_dictionary, key, value):
    a_dictionary[key] = value
    return a_dictionary
