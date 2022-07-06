#!/usr/bin/python3
"""
4-inherits_from: contains inherits from function
"""


def inherits_from(obj, a_class):
    """
    Checks if the object is an instance of a class
    that inherited (directly or indirectly) from the specified class
    Args:
        obj: the object
        a_class: the class
    Return:
        True or False
    """
    if not type(obj) is a_class and issubclass(type(obj), a_class):
        return True
    return False

