#!/usr/bin/python3

"""division of two int a, b"""


def safe_print_division(a, b):
    try:
        result = a / b
    except (TypeError, ZeroDivisionError):
        result = None
    finally:
        print("Inside result: {}".format(result))
        return (result)
