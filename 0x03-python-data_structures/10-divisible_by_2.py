#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    new_list = my_list.copy()
    i = 0

    while my_list and i <= len(new_list) - 1:
        if my_list[i] % 2 == 0:
            new_list[i] = True
        if my_list[i] % 2 != 0:
            new_list[i] = False
        i += 1

    return new_list
