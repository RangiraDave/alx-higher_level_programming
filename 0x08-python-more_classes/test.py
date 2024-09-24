#!/usr/bin/python3
"""Class Rectangle"""


class Rectangle:
    """Its definitions"""


    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__width = value

    def area(self):
        return self.width * self.height
