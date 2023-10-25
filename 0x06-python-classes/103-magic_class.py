#!/usr/bin/python3
"""DEfine a Class"""


import math
class MagicClass:
    """represent a cercle"""
    def __init__(self, radius=0):
        """initialize the magic class"""
        self.__radius = 0
        if type(radius) is  not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """calculates the area of the circle"""
        return ((self.__radius ** 2) * math.pi)

    def circumference(self):
        """caculates the circumfer of the cercle"""
        return (2 * math.pi *self.__radius)
