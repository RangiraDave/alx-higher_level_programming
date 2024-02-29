#!/usr/bin/python3
"""
Script to find a peak element in a list of integers.
"""

def find_peak(list_of_integers):
    """
    Function to find a peak
    """

    lst = list_of_integers

    if not lst or len(lst) is []:
        return None
    if lst[:-1] is lst[len(lst):0]:
        return lst[0]
    s = sorted(lst)
    return s[len(s) - 1]
