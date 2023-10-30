#!/usr/bin/python3
"""DEf classe"""


class Rectangle:
    """represent of rec class"""
    def __init__(self, width=0, height=0):
        """initialiation"""
        self.width = width
        self.height = height

    @property
    def width(self):
        """ to retrieve it"""
        return self.__width

    @width.setter
    def width(self, value):
        """to set it"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        """" to retrieve it"""
        return self.__height

    @height.setter
    def height(self, value):
        """ to set it"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise ValueError('height must be >= 0')
        else:
            self.__height = value

    def perimeter(self):
        """ returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return ((self.__width * 2) + (self.__height * 2))

    def area(self):
        """ returns the rectangle area"""
        return (self.__height * self.__width)
