#!/usr/bin/python3
"""re-implementation of isinstance"""


def is_same_class(obj, a_class):
    """return true if obj is an instance of a_class 
    False otherwise"""
    if (type(obj) is a_class):
        return True
    else:
        return False
