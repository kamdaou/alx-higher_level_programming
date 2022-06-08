#!/usr/bin/python3
def uniq_add(my_list=[]):
    added = []
    result = 0
    if len(my_list) == 0:
        return result
    for element in my_list:
        if element not in added:
            result += element
            added.append(element)
    return result
