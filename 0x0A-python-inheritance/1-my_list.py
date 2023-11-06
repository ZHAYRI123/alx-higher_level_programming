#!/usr/bin/python3
"""
contains print_sorted function
"""


class MyList(list):
    """ a class MyList that inherits from list"""

    def __init__(self):
        """initializes the object"""
        super().__init__()

    def print_sorted(self):
        """prints the sorted list"""
        print(sorted(self))

