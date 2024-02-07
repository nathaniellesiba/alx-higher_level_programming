#!/usr/bin/python3
'''Module to lookup for the method'''

class Student:
    def __init__(self, first_name, last_name, age):
        """
        Instantiate a Student with first_name, last_name, and age.

        Args:
        first_name: The first name of the student.
        last_name: The last name of the student.
        age: The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieve a dictionary representation of a Student instance.

        Args:
        attrs: A list of strings containing attribute names to be retrieved. If None, all attributes are retrieved.

        Returns:
        A dictionary containing the specified or all public instance attributes of the Student instance.
        """
        if attrs is not None and all(isinstance(attr, str) for attr in attrs):
            return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
        else:
            return self.__dict__

