#!/usr/bin/python3
"""base class definition."""


class BaseGeometry(object):
    """This class just raises an exception."""

    def area(self):
        raise Exception("area() is not implemented")
