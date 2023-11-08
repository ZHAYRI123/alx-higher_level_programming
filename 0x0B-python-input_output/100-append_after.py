#!/usr/bin/python3
"""
has append_after fct
"""


import json


def append_after(filename="", search_string="", new_string=""):
    """ inserts a line of text to a file"""
    with open(filename, 'r', encoding='UTF8') as file:
        l_list = []
        while True:
            line = f.readline()
