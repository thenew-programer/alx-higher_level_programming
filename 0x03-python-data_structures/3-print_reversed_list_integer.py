#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    """Print all int of a lst in reverse order."""
    my_list.reverse()
    for i in my_list:
        print("{:d}".format(i))
