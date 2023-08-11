#!/usr/bin/python3

if __name__ == "__main__":
    """This function prints all the names defined by the
    compiled module hidden_4.pyc. It prints one name per line,
    in alphabetical order, excluding names that start with '__'."""

    import hidden_4

    names = dir(hidden_4)
    for name in names:
        if name[:2] != "__":
            print(name)
