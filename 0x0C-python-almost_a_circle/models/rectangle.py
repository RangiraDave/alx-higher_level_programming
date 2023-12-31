#!/usr/bin/python3
"""CLass Rectangle that inherits from Base class."""
from models.base import Base


class Rectangle(Base):
    """Class Rectangle is defined here."""
    def __init__(self, width, height, x=0, y=0, id=None):
        """Its constructor."""
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    @property
    def width(self):
        """Lets get the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """This function sets value of width."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Height getter function"""
        return self.__height

    @height.setter
    def height(self, value):
        """Height setter function"""
        if type(value) is not int:
            raise Exception(TypeError("height must be an integer"))
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Getting the value of x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Function to set the alue of x."""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Getting the value of y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Function to set value of y."""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Function to return area of the rectangle."""
        return self.__width * self.__height

    def display(self):
        """Function to print # and handles x and y."""
        for _ in range(self.__y):
            print("")
        for i in range(self.__height):
            print(" " * self.__x, end='')
            print("#" * self.__width)

    def __str__(self):
        """String to return strings."""
        w = self.__width
        h = self.__height
        name = __class__.__name__
        return f"[{name}] ({self.id}) {self.__x}/{self.__y} - {w}/{h}"

    def update(self, *args, **kwargs):
        """The updater function."""
        if args and len(args) > 0:
            attrib = ['id', 'width', 'height', 'x', 'y']
            for i in range(len(args)):
                setattr(self, attrib[i], args[i])
        else:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)

    def to_dictionary(self):
        """Function to return dict representation of rectangle"""
        i = self.id
        w = self.width
        h = self.height
        x = self.x
        y = self.y
        dic = {
                'id': i,
                'width': w,
                'height': h,
                'x': x,
                'y': y
                }
        return dic
