#!/usr/bin/python3
"""Working on class Rectangle"""


class Rectangle:
    """Here is the definition of class Rectangle"""

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.width * self.height

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return 2 * self.width + 2 * self.height

    def __str__(self):
        if self.height == 0 or self.width == 0:
            return ''
        result = ''
        for _ in range(self.height):
            result += '#' * self.width + '\n'
        return result[:-1]

    def __repr__(self):
        rep = 'Rectangle(' + str(self.width) + ', ' + str(self.height) + ')'
        return rep
