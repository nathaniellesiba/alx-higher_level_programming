#!/usr/bin/python3

import sys

def print_arguments():
arguments = sys.argv[1:]
num_arguments = len(arguments)

if num_arguments == 0:
print("Number of argument(s): 0.")
print(".")
else:
print("Number of argument(s):", num_arguments)
print("Arguments:")
for i, arg in enumerate(arguments):
print(i+1, ":", arg)

if __name__ == "__main__":
print_arguments()
