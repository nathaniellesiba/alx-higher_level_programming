#!/usr/bin/python3

def lookup(obj):
    return dir(obj)

class tsutsa:
    def __init__(self):
        self.x = 5
        self.y = 10
    def some_method(self):
        pass

obj = tsutsa()
print(lookup(obj))

