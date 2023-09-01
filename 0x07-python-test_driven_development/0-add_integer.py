#!/usr/bin/python3
"""define a function called add_integer that it does what it says"""


def add_integer(a, b=98):
    """add 2 integer a and b and return result
    a (int, float): first number
    b (int, float): second number
    """
    if type(a) not in (int, float):
        raise TypeError("a must be an integer")
    if type(b) not in (int, float):
        raise TypeError("b must be an integer")

    return (int(a) + int(b))
