#!/usr/bin/python3
"""
Write a function that writes an Object to
a text file, using a JSON representation
"""
import json


def save_to_json_file(my_obj, filename):
    """
    save to json file
    Args:
        my_obj(str): object to be written in the file
        filename(str): name of the file
    """
    with open(filename, "w") as f:
        json.dump(my_obj, f)
