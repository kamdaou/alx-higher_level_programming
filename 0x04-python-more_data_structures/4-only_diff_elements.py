#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    diff_elmt = []
    for element in set_2:
        if element not in set_1:
            diff_elmt.append(element)
    for element in set_1:
        if element not in set_2:
            diff_elmt.append(element)
    return diff_elmt
