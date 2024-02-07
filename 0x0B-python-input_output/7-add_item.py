#!/usr/bin/python3
'''Module to lookup for the method'''

import sys
from 5-save_to_json_file import save_to_json_file
from 6-load_from_json_file import load_from_json_file

# Add all arguments to a Python list
args_list = sys.argv[1:]

# Load existing data from the file if it exists
try:
    existing_data = load_from_json_file("add_item.json")
except FileNotFoundError:
    existing_data = []

# Add new arguments to the existing list
existing_data.extend(args_list)

# Save the combined list to a file as a JSON representation
save_to_json_file(existing_data, "add_item.json")

