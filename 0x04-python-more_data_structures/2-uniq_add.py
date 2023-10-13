#!/usr/bin/python3
def uniq_add(my_list=[]):
    j = 0
    for i in set(my_list):
        j += i
    return (j)
