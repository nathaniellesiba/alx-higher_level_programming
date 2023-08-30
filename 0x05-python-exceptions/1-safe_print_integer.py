#!/usr/bin/python3
#1-safe_print_integer.py


def safe_print_integer(value):
    """print value which is an int"""
    try:
        print("{:d}".format(value))
        return (True)
    except (TypeError, ValueError):
        return (False)
