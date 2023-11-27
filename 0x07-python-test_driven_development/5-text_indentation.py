#!/usr/bin/python3
"""Function to print 2 new lines after each ., ? and : in a text"""


def text_indentation(text):
    """Function to indent text."""

    if type(text) is not str:
        raise TypeError("text must be a string")

    for i in text:
        print(i, end='')
        if i == '.' or i == '?' or i == ':':
            print("\n")
