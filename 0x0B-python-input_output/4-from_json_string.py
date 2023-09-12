#!/usr/bin/python3
"""
define function from_json_string
"""
import json


def to_json_string(my_obj):
    """
    returns the Python Object representation of a JSON object

    Args:
        my_obj (string): object to be converted
    """
    return json.loads(my_obj)
