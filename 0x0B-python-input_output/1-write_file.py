#!/usr/bin/python3
"""Function to create a file"""


def write_file(filename="", text=""):
    """Function to write to a file."""
    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
