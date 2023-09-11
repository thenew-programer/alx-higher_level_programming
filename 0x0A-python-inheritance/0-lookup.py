#!/usr/bin/python3
"""define a function called lookup"""


def lookup(obj):
    """return a list obj containing all the available
    methods and attributes of a particular object"""
    return list(dir(obj))
