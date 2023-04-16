#!/usr/bin/python3
import json
import sys
"""Adds items to a Python List"""

load_from_json = __import__('6-load_from_json_file').load_from_json_file
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

lent = len(sys.argv)

try:
    data = load_from_json('add_item.json')
except Exception:
    data = []

for i in range(1, lent):
    data.append(sys.argv[i])
save_to_json_file(data, 'add_item.json')
