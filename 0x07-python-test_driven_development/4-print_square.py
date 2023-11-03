#!/usr/bin/python3
def print_square(size):
    if type(size) != int:
        raise TypeError('size must be an integer')
    if size < 0:
        if type(size) == float:
            raise TypeError('size must be an integer')
        else:
            raise TypeError('size must be >= 0')
    for i in range(size):
        print("#" * size, end='')
        print("")
