#!/usr/bin/python3

import sys

"""print the addition of all args."""
def add_arguments():

if len(sys.argv) > 1:

total = 0


for arg in sys.argv[1:]:

num = int(arg)


total += num


print(total)
else:
print("No arguments provided")


add_arguments()
