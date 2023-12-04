#!/bin/python3
"""base class definition."""


class BaseGeometry(object):
    """This class just raises an exception."""

    def __init__(self):
        pass

    def area(self):
        raise Exception("area() is not implemented")
