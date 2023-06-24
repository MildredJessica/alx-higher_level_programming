#!/usr/bin/python3
"""Defines a Student"""


class Student:
    """A class to define a student"""

    def __init__(self, first_name, last_name, age):
        """Creates public instance attributes
        Args
        first_name  (string): Student First name
        last_name (string): Student Last name
        age (int): Age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of a Student instance"""
        return self.__dict__
