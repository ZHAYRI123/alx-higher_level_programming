#!/usr/bin/python3
"""Def class"""

class Rectangle:
    """rep of a rectangle"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """to retrieve it"""
        return self.__width

    @width.setter
    def width(self, value):
        """ to set it"""
        if type(value) is not int:
            raise TypeError('width must be an integer')
        elif value < 0:
            raise ValueError('width must be >= 0')
        else:
            self.__width = value

    @property
    def height(self):
        """ to retrieve it"""
        return self.__height

    @height.setter
    def height(self, value):
        """to set it"""
        if type(value) is not int:
            raise TypeError('height must be an integer')
        elif value < 0:
            raise Value Error('height must be >= 0')
        else:
            self.__height = value

    def area(self):
        """returns the rectangle area"""
        return (self.__width * self.__height)

    def perimeter(self):
        """returns the rectangle perimeter""" 
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return ((self.__height + self.__width) * 2)

    def __str__(self):
        """ print the rectangle with the character #"""
        string = ""
        if self.__width != 0 and self.__height != 0:
            string += "\n".join("#" * self.__width for j in range(self.__height))

        return (string)

    def __repr__(self):
        """return a string representation of the rectangle to be able to recreate a new instance by using eval()"""
        return ("Rectange({:d}, {:d})".format(self.__width, self.__height))
