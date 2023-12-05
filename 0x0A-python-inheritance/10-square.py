#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle
BaseGeometry = __import__('7-base_geometry').BaseGeometry
"""Class Square defined."""


class Square(Rectangle):
    """Square class takes size."""

    def __init__(self, size):
        """Class instantiator."""

        self.__size = size
        BaseGeometry.integer_validator(self, "size", size)

    def area(self):
        return pow(self.__size, 2)

    def __str__(self):
        """Function to return strings given."""

        return f"[Rectangle] {self.__size}/{self.__size}"
