#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is None or not isinstance(roman_string, str):
        return 0
    a_dic = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    roman_int = 0
    i = 0
    while i < len(roman_string):
        if i + 1 < len(roman_string) and a_dic[roman_string[i]] < a_dic[roman_string[i + 1]]:
            roman_int += a_dic[roman_string[i + 1]] - a_dic[roman_string[i]]
            i += 2
        else:
            roman_int += a_dic[roman_string[i]]
            i += 1
    return roman_int
