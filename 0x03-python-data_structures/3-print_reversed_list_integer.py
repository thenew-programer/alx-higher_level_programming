#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """Print all int of a lst in reverse order."""
    for i in my_list[::-1]:
        print("{:d}".format(i))
