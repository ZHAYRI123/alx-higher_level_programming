#!/usr/bin/python3
"""
Adds arguments to a Python list,save them to a file
"""


from sys import argv
save_to_json_file = __import__('5-save_to_json_file.py').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file.py').load_from_json_file

filename = "add_item.json"

try:
    JS_List = load_from_json_file(filename)
except FileNotFoundError:
    JS_List = []

for arg in argv[1:]:
    JS_List.append(arg)

save_to_json_file(JS_List, filename)
