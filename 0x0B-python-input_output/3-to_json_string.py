#!/usr/bin/python3
"""
define function to_json_string
"""
import json


def to_json_string(my_obj):
    """
    returns the JSON representation of an object (string)

    Args:
        my_obj (string): object to be converted
    """
    return json.dumps(my_obj)
