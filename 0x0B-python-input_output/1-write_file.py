#!/usr/bin/python3
"""Function to create a file"""


def write_file(filename="", text=""):
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
