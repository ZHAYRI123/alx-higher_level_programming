#!/usr/bin/python3
"""student class"""


class Student:
    """student representation"""
    def __init__(self, first_name, last_name, age):
        """instantiation with first_name, last_name"""
        self.first_name  = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ retrieves a dictionary representation"""
        return (self.__dict__)
