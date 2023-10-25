#!/usr/bin/python3
def safe_function(fct, *args):
    try:
        res = fct(*args)
        return (res)
    except Exception as error:
        import sys
        print("Exceptio: {}".format(error), file=sys.stderr)
        return None
