#!/usr/bin/python3
def safe_print_integer(value):
    try:
        print("{:d}".format(value))
    except (TypeError, ValueError, IndexError):
        return False
    return True
