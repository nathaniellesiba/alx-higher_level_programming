#!/usr/bin/python3

"""takes a list as input, uses the set() function to remove"""
"""duplicate elements, leaving only unique int. Then, the sum() function"""
"""is used to calculate the sum of all the unique integers in the list"""
""". Finally, the sum is returned as the output"""


def uniq_add(my_list=[]):
    return sum(set(my_list))
