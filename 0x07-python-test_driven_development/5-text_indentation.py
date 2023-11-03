#!/usr/bin/python3
def text_indentation(text):
    if type(text) != str:
        raise TypeError('text must be a string')
    for i in range(len(text)):
        if text[i] != '.' and text[i] != ':' and text[i] != '?':
            print(text[i], end='')
        else:
            print(text[i])
            print("")
