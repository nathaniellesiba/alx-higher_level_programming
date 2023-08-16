#!/usr/bin/python3


"""This code defines a function multiply_list_map that takes two parameters: my_list (a list of values) and number (the number to multiply each value by). The function uses the map function to apply the lambda function lambda x: x * number to each element in my_list. The result is a new list where each value is multiplied by number. The function returns this new list.

Note that the code uses a lambda function within the map function to perform the multiplication operation. The map function applies this lambda function to each element in my_list, effectively multiplying each value by number. Finally, the list function is used to convert the map object into a list."""

def multiply_list_map(my_list=[], number=0):
    return list(map(lambda x: x * number), my_list)
