#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        for i in range(x):
            print("{:d}".format(my_list[i]), end=" ")
            count += 1
    except (ValueError, IndexError, TypeError):
        continue
    finally:
        print("")
        return (count)
