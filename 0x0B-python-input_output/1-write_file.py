#!/usr/bin/python3
"""
define a function called write_file
"""


def write_file(filename="", text=""):
    """
    write to a file

    Args:
        filename (str): filename to be read
        text (str): text to be written into the file
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
