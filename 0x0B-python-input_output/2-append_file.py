#!/usr/bin/python3
"""
define a function called append_file
"""


def append_file(filename="", text=""):
    """
    write to a file and append if the file already exists

    Args:
        filename (str): filename to be read
        text (str): text to be written into the file
    """
    with open(filename, mode="a", encoding="utf-8") as f:
        f.write(text)
