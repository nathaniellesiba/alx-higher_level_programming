#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
""" Adds two tuples and returns a new tuple with the sum of the corresponding elements.
 
Args:
        tuple_a (tuple): The first tuple.
        tuple_b (tuple): The second tuple.
    
Returns:
        tuple: A new tuple with the sum of the corresponding elements."""
"""If a tuple is smaller than 2, use 0 for each missing integer"""
    if len(tuple_a) < 2:
        tuple_a += (0,) * (2 - len(tuple_a))
    if len(tuple_b) < 2:
        tuple_b += (0,) * (2 - len(tuple_b))
    
"""Add corresponding elements frm each tuple"""
    sum_tuple = (tuple_a[0] + tuple_b[0], tuple_a[1] + tuple_b[1])
    
    return sum_tuple
