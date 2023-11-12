#!/usr/bin/python3
"""DEfine a rectangle class"""
from models.base import Base


class Rectangle(Base):
    """Represent a Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a Rectangle"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """get the width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        """set the width"""
        if type(value) == str:
            raise TypeError("The value musn't be a str")
        if value <= 0:
            raise ValueError("the width must be > 0")
        self.__width = value

    @property
    def height(self):
        """get height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """set the height"""
        if type(value) == str:
            raise TypeError("height musn't be a str")
        if value <= 0:
            raise ValueError("Height must be > 0")
        self.__height = value

    @property
    def x(self):
        """get x value"""
        return (self.__x)

    @x.setter
    def x(self, value):
        """set the x"""
        if type(value) == str:
            raise TypeError("X must be a number")
        if value < 0:
            raise ValueError("x must be > 0")
        self.__x = value

    @property
    def y(self):
        """get y value"""
        return (self.__y)

    @y.setter
    def y(self, value):
        """set the y"""
        if type(value) == str:
            raise TypeError("y must be a number")
        if value <= 0:
            raise ValueError("y  must be > 0")
        self.__y = value
