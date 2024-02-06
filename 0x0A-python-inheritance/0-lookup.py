#!/usr/bin/python3

def lookup(obj):
    return dir(obj)

class Example:
    def __init__(self):
        self.x = 5
        self.y = 10
    def some_method(self):
        pass

obj = Example()
print(lookup(obj))
