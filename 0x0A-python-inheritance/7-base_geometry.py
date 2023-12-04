#!/usr/bin/python3
"""Base class with value validator."""


class BaseGeometry(object):
    """Defining the class."""

    def area(self):
        """Function to raise an exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Function to validate value."""

        if type(value) is not int:
            raise TypeError("<name> must be an integer")
        if value <= 0:
            raise ValueError("<name> must be greater than 0")

        self.name = name
        self.value = value

