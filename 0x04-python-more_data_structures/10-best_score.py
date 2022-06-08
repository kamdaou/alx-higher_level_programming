#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    key_list = list(a_dictionary.keys())
    val_list = list(a_dictionary.values())
    score = max(a_dictionary.values())
    position = val_list.index(score)
    return key_list[position]
