#!/usr/bin/python3
"""
has a read fct
"""


def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout"""

    with open(filename, 'r', encoding='UTF8') as file:
        print(file.read())
