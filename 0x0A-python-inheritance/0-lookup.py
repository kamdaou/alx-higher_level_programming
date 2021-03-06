#!/usr/bin/python3
"""
    0-lookup: lookup()
"""


def lookup(obj):
    """
    Return list of attribute and method of the object
    Args:
        obj: the object
    Return:
        list of attributes and method
    """
    return dir(obj)
