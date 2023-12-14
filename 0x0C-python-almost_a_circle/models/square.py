#!/usr/bin/python3
""" the class Square"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """to initialize"""
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """get the set value"""
        return (self.width)

    @size.setter
    def size(self, value):
        """set the size value"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """assigns attributes"""
        if len(args) != 0:
            a = 0
            for arg in args:
                if a == 0:
                    if arg == None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = arg
                elif a == 1:
                    self.size = arg
                elif a == 2:
                    self.x = arg
                elif a == 3:
                    self.y = arg
                a += 1
        elif len(kwargs) != 0:
            for k, v in kwargs.items():
                if k == "id":  
                    self.id = v
                elif k == "size":
                    self.size = v
                elif k == "x":
                    self.x = v
                elif k == "y":
                    self.y = v
    def __str__(self):
        """rep of the square"""
        return (f"[Square] ({self.id}) {self.x}/{self.y} - {self.size}")

    def to_dictionary(self):
        """ returns the dictionary representation of a Square"""
        return ({
            "id": self.id,
            "size": self.size,
            "x": self.x,
            "y": self.y
            })
