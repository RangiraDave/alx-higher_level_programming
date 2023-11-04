#!/usr/bin/python3
def no_c(my_string):
    s_list = [i for i in my_string if i != 'c' and i != 'C']
    new_str = ''
    for i in s_list:
        new_str += i
    return new_str
