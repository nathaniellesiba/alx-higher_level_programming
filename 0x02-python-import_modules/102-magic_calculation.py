#!/usr/bin/python3
def magic_calculation(a, b):
    from magic_calculation_102 import add, sub

    if a < b:
        n = range(4, 6)
        t = add(a, b)
        for s in n:
            t = add(t, s)
        return(t)
    else:
        return(sub(a, b))
