#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    m = len(sys.argv) - 1
    print("{} argument".format(m), end='')
    if m == 0:
        print("s.")
    elif m > 1:
        print("s:")
    else:
        print(":")
    for i in range(m):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
