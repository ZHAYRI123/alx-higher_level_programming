#!/usr/bin/python3
def read_file(filename=""):
    """reads a text file (UTF8) and prints it to stdout"""

    with open('UTF8', 'r') as file:
        print(file.read())
