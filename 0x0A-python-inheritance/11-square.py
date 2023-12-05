#!/usr/bin/python3
"""Class Square updated to handle print and str"""
Rectangle = __import__('9-rectangle').Rectangle
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(Rectangle):
    """Definition of the Square class."""

    def __init__(self, size):
        """Instantiation of size."""

        self.__size = size
        BaseGeometry.integer_validator(self, "size", self.__size)

    def area(self):
        """Function to compute area."""

        return pow(self.__size, 2)

    def __str__(self):
        """Function to handle str."""

        return f"[Square] {self.__size}/{self.__size}"
