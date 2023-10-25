#!/usr/bin/python3
"""Define classes"""


class Square:
    """square class"""

    def __init__(self, size=0):
        """initialise size value"""
        self.__size = size
    
    def area(self):
        """square value"""
        return (self.__size ** 2)

    @property
    def size(self):
        """retrieve size"""
        return self.__size

    @size.setter
    def size(self, value):
        """property setter of size"""
        if value < 0:
            raise ValueError('size must be >= 0')
        elif not isinstance(value, int):
            raise TypeError('size must be an integer')
        else:
            self.__size = value
