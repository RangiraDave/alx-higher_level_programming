#!/usr/bin/python3
# Script to find a peak element in a list of integers.

def find_peak(list_of_integers):
    # Function to find a peak

    l = list_of_integers

    if not l or len(l) is []:
        return None
    if l[:-1] is l[len(l):0]:
        return l[0]
    s = sorted(l)
    return s[len(s) - 1]

if __name__ == "__main__":
    find_peak(list_of_integers)
