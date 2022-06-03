#!/usr/bin/python3
def no_c(my_string):
    new_str = ""
    for elt in my_string:
        if elt != 'c' and elt != 'C':
            new_str += elt
    return new_str
