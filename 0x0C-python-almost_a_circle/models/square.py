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

    def __str__(self):
        """rep of the square"""
        return (f"[Square] ({id}) {x}/{y} - {size}")
