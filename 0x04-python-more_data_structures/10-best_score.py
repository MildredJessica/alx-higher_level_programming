#!/usr/bin/python3

def best_score(a_dictionary):
    """Returns a key with the biggest integer value"""
    if a_dictionary == None:
        return None
    score = max(a_dictionary.values())
    key = ""
    for k,v in a_dictionary.items():
        if v == score:
            key = k
    return key
