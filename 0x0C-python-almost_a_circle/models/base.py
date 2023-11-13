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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representation"""
        m = []
        if (list_dictionaries is not None or list_dictionaries != []):
            m = json.dumps(list_dictionaries)
        return (m)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes the JSON string representation to a file"""
        filename = cls.__name__ + ".json"
        with open(filename, "w") as jsfile:
            if list_objs is None:
                jsfile.write("[]")
            else:
                list_dic = [m.to_dictionary() for m in list_objs]
                jsfile.write(Base.to_json_string(list_dic))

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation"""
        if (json_string is None or json_string == []):
            return ([])
        else:
            return (json.loads(json_string))

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set"""
        if dictionary != {} and dictionary:
            if cls.__name__ == "Rectangle":
                n = cls(1, 1)
            else:
                n = cls(1)
            n.update(**dictionary)
            return (n)

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances"""
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, 'r') as jsfile:
                dic_list = Base.from_json_string(jsonfile.read())
                return [cls.creat(**m) for m in dic_list]
        except IOError:
            return ([])

