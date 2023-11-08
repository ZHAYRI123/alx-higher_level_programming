#!/usr/bin/python3
"""
Define class stud
"""


class student:
    """Rep a student"""

    def __init__(self, first_name, last_name, age):
        """Instantiation with first_name, last_name"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Dict representation"""
        if (type(attrs) == list and
                all(type(item) == str for item in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

