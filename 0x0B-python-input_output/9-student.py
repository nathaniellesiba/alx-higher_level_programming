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

    def to_json(self):
        """
        Retrieve a dictionary representation of a Student instance.

        Returns:
        A dictionary containing the public instance attributes of the Student instance.
        """
        serializable_dict = {}
        for key, value in self.__dict__.items():
            if isinstance(value, (str, int)):
                serializable_dict[key] = value
        return serializable_dict

