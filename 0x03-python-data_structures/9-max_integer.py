#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list == []:
        return 'None'

    if my_list:
        comp = 0
        for n in my_list:
            if n >= comp:
                comp = n
        return comp
    else:
        return 'None'
