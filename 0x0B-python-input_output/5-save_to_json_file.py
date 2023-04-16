#!/usr/bin/python3
"""Writes an object to a text file using JSON representation"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using a JSON representation
    Args
    my_obj (String)
    filename (string): File name
    """
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(my_obj, f)
