#!/usr/bin/python3
"""
has a load_from_json_file fct 
"""


import json


def load_from_json_file(filename):
    """ creates an Object from a JSON file"""
    with open(filename, 'r', encoding="UTF8") as file:
        return (json.load(file))
