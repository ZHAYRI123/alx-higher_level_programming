#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    if len(tuple_a) < 2:
        if len(tuple_a) == 0:
            tuple_a = 0, 0
        else:
            typle_a = typle_a[0], 0
    if len(tuple_b) < 2:
        if len(tuple_b) == 0:
            tuple_b = 0, 0
        else:
            typle_b = typle_b[0], 0
    add_typle = typle_a[0] + typle_b[0], typle_a[1] + typle_b[1]
    return(add_typle)
~
