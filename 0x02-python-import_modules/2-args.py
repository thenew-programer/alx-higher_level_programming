#!/usr/bin/python3

if __name__ == "__main__":
    import sys

    lenght = len(sys.argv) - 1
    args = sys.argv[1:]
    if (lenght == 0):
        print("0 argument.")
    elif (lenght == 1):
        print("1 argument:")
    else:
        print("{} arguments:".format(lenght))

    for i, arg in enumerate(args, start=1):
        print("{}: {}".format(i, arg))
