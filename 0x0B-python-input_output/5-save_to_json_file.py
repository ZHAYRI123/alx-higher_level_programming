#!/usr/bin/python3
"""
has a save_to_json_file fct
"""


import json


def save_to_json_file(my_obj, filename):
    """ writes an Object to a text file"""
    with open(filename, 'w') as file:
        return (json.dump(my_obj, file)
