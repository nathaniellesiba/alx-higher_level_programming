#!/usr/bin/python3

import string

def print_alphabet():
"""This function prints the alphabet in
uppercase, followed by a new line.
"""
print(*string.ascii_uppercase, sep='', end='\n')
