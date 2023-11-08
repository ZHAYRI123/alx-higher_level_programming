#!/usr/bin/python3
"""contains inherits_from fct"""


def inherits_from(obj, a_class):
    """True if it's an instance of a class that inherited"""
    if type(obj) == a_class:
        return (False)
    else:
        return (True)
