#!/usr/bin/python3

def safe_print_integer(value):
value = 0

try:

print("{:d}".format(0))
return (True)

except(TypeError, ValueError):

return (False)
