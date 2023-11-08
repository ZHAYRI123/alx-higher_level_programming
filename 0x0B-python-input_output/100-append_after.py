#!/usr/bin/python3
"""
has append_after fct
"""


def append_after(filename="", search_string="", new_string=""):
    """ inserts a line of text to a file"""
    with open(filename, 'r', encoding='UTF8') as file:
        l_list = ""
        while filename:
            li = file.readline()
            if li == "":
                break
            l_list += li
            if search_string in li:
                l_list += (new_string)
    with open(filename, 'w', encoding='UTF8') as file:
        file.writelines(l_list)
