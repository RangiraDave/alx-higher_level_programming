#!/usr/bin/python3
"""Function to read a file"""


def read_file(filename=""):
    """This function uses with"""
    with open(filename, 'r', encoding = 'utf-8') as f:
        for i in f:
            print(i)
