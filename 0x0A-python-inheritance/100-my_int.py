#!/usr/bin/python3
"""
class MyInt that inherits from int
"""


class MyInt(int):
    """ is a rebel. MyInt has == and != operators inverted"""

    def __init__(self, s):
        """ initialize s"""
        super().__init__()

    def __eq__(self, x):
        """comprision methode"""

        return (not super().__eq__(self))

    def __ne__(self, x):
        """comprision methode"""

        return (not super().__ne__(self))
