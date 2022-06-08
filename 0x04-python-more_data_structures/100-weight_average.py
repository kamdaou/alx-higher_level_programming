#!/usr/bin/python3
def weight_average(my_list=[]):
    up = 0
    down = 0
    for element in my_list:
        up += element[0] * element[1]
        down += element[1]
    return up/down
