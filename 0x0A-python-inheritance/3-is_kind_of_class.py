#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    """
    Checks if the object is an instance of,
    or if the object is an instance of a class that inherited from,
    the specified class
    Args:
        abj: the object
        a_class: the class
    Return:
        True or false.
    """
    if isinstance(obj, a_class):
        return True
    return False
