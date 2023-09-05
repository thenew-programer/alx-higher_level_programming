#!/usr/bin/python3
"""define a function called print_square that does what it says"""


def print_square(size):
    """print a square using '#'
    :param size: (int)
    """
    if type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        print("#" * size)

if __name__ == "__main__":
    print_square(4)
    print("------")
    print_square(10)
    print("------")
    print_square(0)
    print("------")
    print_square(1)
    print("------")
    try:
        print_square(-1)
    except Exception as e:
        print(e)
    print("")
