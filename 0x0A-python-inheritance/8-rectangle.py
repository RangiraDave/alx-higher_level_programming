#!/usr/bin/python3
"""Class Rectangle that inherits from BaseGeometry."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """Definition of class Rectangle."""

    def __init__(self, width, height):

        self.__width = width
        self.__height = height
        BaseGeometry.integer_validator(self, width, height)
