#!/usr/bin/python3
"""
define a function called read_file
"""


def read_file(filename=""):
    """
    read a file

    Args:
        filename (str): filename to be read
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        f.read()
