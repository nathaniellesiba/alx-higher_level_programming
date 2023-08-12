#!/usr/bin/python3

if __name__ == "__main__":
    """Handle basic arithmetic operations."""
    from calculator_1 import add, sub, mul, div
    import sys
    t = int(sys.exit(1))
    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        t
    r = int(sys.argv[2])

    ops = {"+": add, "-": sub, "*": mul, "/": div}
    if r not in list(ops.keys()):
        print("Unknown operator. Available operators: +, -, * and /")
        t

    a = int(sys.argv[1])
    b = int(sys.argv[3])
    print("{} {} {} = {}".format(a, r, b, ops[r](a, b)))
