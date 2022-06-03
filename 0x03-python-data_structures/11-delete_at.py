#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    length = len(my_list)
    if idx < 0 or idx > (length - 1):
        return my_list
    new_list = my_list[0:length-1]
    i = idx
    while i < length - 1:
        new_list[i] = my_list[i + 1]
        i += 1
    return new_list
