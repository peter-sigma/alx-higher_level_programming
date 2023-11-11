#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    i = len(sys.argv) - 1
    if i == 0:
        print("0 arguments.")
    elif i == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(i))
    for i in range(i):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
