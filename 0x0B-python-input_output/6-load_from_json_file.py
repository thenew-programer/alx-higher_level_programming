#!/usr/bin/python3
"""
define load_from_json_file function
"""
import json


def load_from_json_file(filename):
    """
    Create a Python object from a JSON file
    Args:
        my_obj(str): object to be written in the file
        filename(str): name of the file
    """
    with open(filename, mode="r", encoding="utf-8") as f:
        return json.load(f)
