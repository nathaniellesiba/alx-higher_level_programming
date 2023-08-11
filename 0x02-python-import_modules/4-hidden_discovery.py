#!/usr/bin/python3

"""
This function prints all the names defined by the compiled module hidden_4.pyc.
It prints one name per line, in alphabetical order, excluding names that start with '__'.
"""

import hidden_4

names = dir(hidden_4)
sorted_names = sorted(names)
for name in sorted_names:
if not name.startswith('__'):
print(name)

