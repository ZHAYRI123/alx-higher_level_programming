#!/usr/bin/python3
"""
 a class BaseGeometry (based on 6-base_geometry.py)
 """


class BaseGeometry:
    """has two public instance"""

    def area(self):
        """public methode that raise a exception"""

        raise Exception('area() is not implemented')
    def integer_validator(self, name, value):
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        elif value < 0 or value == 0:
            raise ValueError(f"{name} must be greater than 0")
