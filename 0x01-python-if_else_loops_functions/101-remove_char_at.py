#!/usr/bin/python3

def remove_char_at(str, n):
    """Creates a copy of the string, removing 
    the character at the position n
    """
    return (str[:n] + str[n+1:])
