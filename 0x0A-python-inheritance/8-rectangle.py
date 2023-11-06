#!/usr/bin/python3
"""
class Rectangle that inherits from BaseGeometry
"""


class Rectangle:
    """calss has 2 methode"""

    def __init__(self, width, height):
        """Instantiation with width and height"""
        self.__width = width
        self.__height = height

    def integer_validator(self, name, value):
        """width and height must be positive integers, validated by integer_validator"""
        super().integer_validator(self, name, value)
