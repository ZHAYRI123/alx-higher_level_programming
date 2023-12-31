#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    from calculator_1 import add, sub, div, mul
    count = len(sys.argv)
    if count - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        sys.exit(1)
    else:
        opr = {"+": add, "-": sub, "*": mul, "/": div}
        if sys.argv[2] not in list(opr.keys()):
            print("Unknow operator. Available operators: +, -, * and /")
            sys.exit(1)
        else:
            a = int(sys.argv[1])
            b = int(sys.argv[3])
            print("{:d} {} {:d} = {:d}".format(a, sys.argv[2], b, opr[sys.argv[2]](a, b)))
