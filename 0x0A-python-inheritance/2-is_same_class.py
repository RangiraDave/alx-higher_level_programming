#!/usr/bin/python3
"""
Function to check whether an object is an instance of a class provided.
"""


def is_same_class(obj, a_class):
    """Returns True if it is and False otherwise"""

    return type(obj) is a_class
