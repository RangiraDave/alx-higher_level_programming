#!/usr/bin/python3
"""
Function to check whether an object is
kinda an instance of a class provided.
"""


def is_kind_of_class(obj, a_class):
    """Returns True if it is and False otherwise"""
    return isinstance(obj, a_class)
