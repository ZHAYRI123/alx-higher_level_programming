#!/usr/bin/python3
c = 0
for i in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(i - c)), end='')
    if c == 0:
        c = 32
    else:
        c = 0
