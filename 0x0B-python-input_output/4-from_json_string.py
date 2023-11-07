#!/usr/bin/python3
"""
has Json fct
"""


import json


def from_json_string(my_str):
    """function that returns an object (Python data structure)"""
    return json.loads(my_str)
