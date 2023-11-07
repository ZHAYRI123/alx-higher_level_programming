#!/usr/bin/python3
def write_file(filename="", text=""):
    """writes a string to a text file"""
    with open(filename, 'w', encoding='UTF8') as file:
        file.write(text)
        count = len(text)
    return (count)
