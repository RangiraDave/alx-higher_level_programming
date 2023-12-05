#!/usr/bin/python3
"""Function to append text to a file."""


def append_write(filename="", text=""):
    """The function definition."""

    with open(filename, 'r+', encoding="utf-8") as f:
        return f.write(str(text))
