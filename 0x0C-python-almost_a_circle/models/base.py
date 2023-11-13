#!/usr/bin/python3
""" the first class Base"""
import json
import csv
import turtle


class Base:
    """Represent the Base model"""

    __nb_objects = 0
    def __init__(self, id=None):
        """Initialise a new Base"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    def to_json_string(list_dictionaries):
        """ returns the JSON string representation"""
        m = []
        if (list_dictionaries is not None or list_dictionaries != []):
            m = json.dumps(list_dictionaries)
        return (m)
