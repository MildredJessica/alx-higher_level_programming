#!/usr/bin/python3
"""Returns an object (Python data structure) represented by a JSON string"""
import json

def from_json_string(my_str):
    """Returns an object represented by a JSON string
    Args
    my_str (String)
    """
    return json.loads(my_str)
