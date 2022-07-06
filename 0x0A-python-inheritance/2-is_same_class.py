#!/usr/bin/python3
"""
2-is_same_class: is the same class
"""


def is_same_class(obj, a_class):
    """
    Returns true if the object obj is an instance of the class a_class
    Args:
        obj: the given object
        a_class: the class
    Return:
        True or False.
    """
    if type(obj) is a_class:
        return True
    return False
