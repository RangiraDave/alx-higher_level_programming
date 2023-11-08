#!/usr/bin/python3

def uniq_add(my_list=[]):
    temp, add = [], 0
    for i in my_list:
        if i in temp:
            continue
        temp.append(i)

    for i in temp:
        add += i
    return add
