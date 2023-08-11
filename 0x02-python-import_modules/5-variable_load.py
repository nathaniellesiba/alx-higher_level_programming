#!/usr/bin/python3

def print_variable_from_file():
"""
This function imports the variable 'a'
from the file 'variable_load_5.py' and
prints its value.
It follows the guidelines of not
using '*' for importing or '__import__'
The code is not executed when imported.
"""

from variable_load_5 import a


print(a)
except ImportError as e:

print(f"Error: {e}")
