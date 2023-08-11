#!/usr/bin/python3

if __name__ == "__main__":
    """prints the number of and the list of its arguments."""
    import sys

    tot = len(sys.argv) - 1
    if tot == 0:
        print("0 arguments.")
    elif tot == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(tot))
    for j in range(tot):
        print("{}: {}".format(j + 1, sys.argv[j + 1]))
