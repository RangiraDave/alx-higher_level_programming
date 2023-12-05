#!/usr/bin/python3
"""Does it inherit from class?"""


def inherits_from(obj, a_class):
    """This function takes odj and a_class"""

    return type(obj) is not a_class and issubclass(type(obj), a_class)
