#!/usr/bin/python3

"""The function takes dictionary name a_dictionary as input and uses the len() function along with the keys() method to calculate the number of keys in the dictionary. The keys() method returns a view object that contains all the keys in the dictionary, and the len() function returns the length of this view object, which gives us the count of keys in the dictionary."""

def number_keys(a_dictionary):
    return len(a_dictionary.keys())
