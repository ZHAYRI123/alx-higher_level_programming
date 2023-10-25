#!/usr/bin/python3
"""Defines square class"""


class Square:
    """class represent a square"""

    def __init__(self, size=0):
        """initialisation class
        args: size - the size of a square
        raises TypeError or ValueError"""
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
