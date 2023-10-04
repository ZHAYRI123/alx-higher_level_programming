#!/usr/bin/python3
def pow(a, b):
    if b == 0:
        return (1)
    else:
        pow = 1
        for i in range(0, abs(b)):
            pow = a * pow
        if b > 0:
            return (pow)
        else:
            return (1 / pow)
