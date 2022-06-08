#!/usr/bin/python3
def common_elements(set_1, set_2):
    c_set = []
    for el_1 in set_1:
        if el_1 in set_2:
            c_set.append(el_1)
    return c_set
