def multiply_by_2(a_dictionary):
    new_dictionary = {}
    for keys in a_dictionary:
        new_dictionary[keys] = a_dictionary[keys] * 2
    return new_dictionary
