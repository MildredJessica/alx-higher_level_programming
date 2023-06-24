#!/usr/bin/python3
"""Checks for a list of available attributes"""


def lookup(obj):
    """"Returns a list of available objects"""
    return dir(obj)
