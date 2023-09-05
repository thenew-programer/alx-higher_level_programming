#!/usr/bin/python3
"""define a function called magic_string"""


def magic_string():
    """prints a string and increment each time we call the function"""
    magic_string.i = getattr(magic_string, "i", 0) + 1
    return "BestSchool, " * (magic_string.i - 1) + "BestSchool"
