#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    temp = sorted(a_dictionary)
    for i in temp:
        print("{}: {}".format(i, a_dictionary[i]))
