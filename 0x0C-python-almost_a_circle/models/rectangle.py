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
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """get height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """set the height"""
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """get x value"""
        return (self.__x)

    @x.setter
    def x(self, value):
        """set the x"""
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """get y value"""
        return (self.__y)

    @y.setter
    def y(self, value):
        """set the y"""
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y  must be >= 0")
        self.__y = value

    def area(self):
        """ returns the area value of the Rectangle"""
        return (self.width * self.height)

    def display(self):
        """prints in stdout the Rectangle instance with:#"""
        if self.width == 0 or self.height == 0:
            print("")
            return
        for i in range(self.y):
            print("")
        for i in range(self.height):
            print("" * self.x, end="")
            print("#" * self.width, end="")
            print("")

    def update(self, *args, **kwargs):
        """ assigns an argument to each attribute:"""
        if len(args) != 0:
            m = 0
            for arg in args:
                if m == 0:
                    if arg == None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arg
                elif m == 1:
                    self.width = arg
                elif m == 2:
                    self.height = arg
                elif m == 3:
                    self.x = arg
                elif m == 4:
                    self.y = arg
                m += 1
        elif len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":
                    if v == None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = v
                elif k == "width":
                    self.width = v
                elif k == "height":
                    self.height = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v

    def __str__(self):
        """returns:[Rectangle] id x/y - width/height"""
        return (f"({self.id}) {self.x}/{self.y} - {self.width}/{self.height}")
