#!/usr/bin/python3
"""
 function that adds a new attribute to an object
 """


def adds_new_attribute(obj, name, value):
    """a function that adds a new attribute to an object if it’s possible"""

    if not isinstance(obj, dict):
        raise TypeError("can't add new attribute")
    else:
        obj[name] = value
