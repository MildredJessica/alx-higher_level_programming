#!/usr/bin/python3
"""A function that creates an Object from a “JSON file”"""
import json


def load_from_json_file(filename):
    """Creates an object from a JSON file
    Args
    filename (string): The name of the file
    """
    with open(filename, 'r', encoding='utf-8') as f:
        x = json.load(f)
    return x
