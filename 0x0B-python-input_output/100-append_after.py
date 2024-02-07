#!/usr/bin/python3
'''Module to lookup for the method'''


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file after each line containing a specific string.

    Args:
    filename: The name of the file.
    search_string: The specific string to search for in the file.
    new_string: The line of text to insert after each line containing the search_string.
    """
    # Open the file in read mode and create a temporary file to store the modified content
    with open(filename, 'r') as file, open(filename + '.tmp', 'w') as temp_file:
        # Read the file line by line
        for line in file:
            # Write the original line to the temporary file
            temp_file.write(line)
            # If the search_string is found in the line, insert the new_string after it
            if search_string in line:
                temp_file.write(new_string + '\n')

    # Rename the temporary file to the original file
    import os
    os.rename(filename + '.tmp', filename)

