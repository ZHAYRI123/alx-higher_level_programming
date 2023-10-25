#!/usr/bin/python3
"""Define a Class"""


class Square:
    """Square class"""

    def __init__(self, size=0):
        """initializing a square size
        Args: size - square size
        raises: TypeError or Valueerror"""
        if size < 0:
            raise ValueError('size must be >= 0')
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        self.__size = size
    def area(self):
        """ returns the current square area"""

        return (self.__size ** 2)
