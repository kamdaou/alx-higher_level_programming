#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    max_val = my_list[0]
    for elt in my_list:
        if elt > max_val:
            max_val = elt
    return max_val
