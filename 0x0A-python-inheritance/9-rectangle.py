#!/usr/bin/python3
"""The Rectangle implements area and prints it."""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class definition."""

    def __init__(self, width, height):
        """Class Rectangle insitantiation."""

        self.__width = width
        self.__height = height
        BaseGeometry.integer_validator(self, "width", width)
        BaseGeometry.integer_validator(self, "height", height)

    def area(self):
        """Function to return the area of the rectangle."""

        return self.__width * self.__height

    def __str__(self):
        """Special method to return strings given."""

        return f"[Rectangle] {self.__width}/{self.__height}"
