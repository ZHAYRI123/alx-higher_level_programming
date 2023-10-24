#!/usr/bin/python3
"""Define classes"""

class Square:
    """square class"""

    def __init__(self, size=0):
        """initialise size value
        args: size - squares size
        raise: TypeError or Valueerror"""
        if size < 0:
            raise ValueError('size must be >= 0')
        if not isinstance(size, int):
            raise TypeError('size must be an integer')
        self.__size = size
        
        @property
        def size(self):
            """retrieve size"""
            return self.__size

        @size.setter
        def size(self, value):
            if size < 0:
                raise ValueError('size must be >= 0')
            if not isinstance(size, int):
                raise TypeError('size must be an integer')
            self.__size = size
        def area(self):
            """square value"""
            return (self.__size ** 2)
