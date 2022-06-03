#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if idx < 0 or idx > (len(my_list) - 1):
        return my_list
    new_list = []
    for elt in my_list:
        if len(new_list) == idx:
            new_list.append(element)
        else:
            new_list.append(elt)
    return new_list
