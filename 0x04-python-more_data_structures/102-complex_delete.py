#!/usr/bin/python3


"""The function takes 2 parameters: a_dictionary (the dictionary to be modified) and value (the value to be searched and deleted). It initializes an empty list keys_to_delete to store the keys that need to be deleted.

Next, it iterates over each key-value pair in the dictionary using the items() method. If the value of the current key matches the specified value, the key is added to the keys_to_delete list.

After iterating through all the key-value pairs, the function then iterates over the keys_to_delete list and deletes each key from the dictionary using the del statement.

Finally, the modified dictionary is returned as the output of the function.

This function allows us to easily delete all keys with a specific value in a dictionary without the need for any external modules."""


def complex_delete(a_dictionary, value):
    keys_to_delete = []
    for key, val in a_dictionary.items():
        if val == value:
            keys_to_delete.append(key)
    for key in keys_to_delete:
        del a_dictionary[key]
    return a_dictionary
