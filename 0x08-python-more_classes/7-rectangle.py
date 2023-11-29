#!/usr/bin/python3
"""Working on class Rectangle"""


class Rectangle:
    """Here is the definition of class Rectangle"""

    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        self.__width = width
        self.__height = height
        Rectangle.number_of_instances += 1
        self.__print_symbol = None

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

    @property
    def print_symbol(self):
        if self.__print_symbol is None:
            return '#'#Rectangle.print_symbol
        else:
            return self.__print_symbol

    @print_symbol.setter
    def print_symbol(self, value):
        self.__print_symbol = value

    def __str__(self):
        if self.height == 0 or self.width == 0:
            return ''
        result = ''
        for _ in range(self.__height):
            result += str(self.print_symbol) * self.__width + '\n'
        return result[:-1]

    def __repr__(self):
        rep = 'Rectangle(' + str(self.width) + ', ' + str(self.height) + ')'
        return rep

    def __del__(self):
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
