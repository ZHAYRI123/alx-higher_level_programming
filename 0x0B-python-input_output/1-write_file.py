#!/usr/bin/python3
"""
has write fct
"""


def write_file(filename="", text=""):
    """writes a string to a text file"""
    with open(filename, 'w', encoding='UTF8') as file:
        return (file.write(text))
