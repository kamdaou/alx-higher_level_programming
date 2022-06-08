#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    while value in a_dictionary.values():
        key_list = list(a_dictionary.keys())
        val_list = list(a_dictionary.values())
        pos = val_list.index(value)
        key = key_list[pos]
        del a_dictionary[key]
    return a_dictionary
