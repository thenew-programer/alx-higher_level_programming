#!/usr/bin/python3
"""

"""
import json


def save_to_json_file(my_obj, filename):
    """
    Args:
        my_obj(str): object to be written in the file
        filename(str): name of the file
    """
    with open(filename, mode="w", encoding="utf-8") as f:
        return f.write(json.dumps(my_obj))
