#!/usr/bin/python3

def weight_average(my_list=[]):
    if my_list == []:
        return 'None'
    sm, ml = 0, 0
    for row in my_list:
        ml += row[0] * row[1]
        sm += row[1]

    return ml / sm
