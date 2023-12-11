#!/usr.bin/python3
"""CLass Square that iniherits form our Rectangle class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class definition."""
    def __init__(self, size, x=0, y=0, id=None):
        width = size
        height = size
        super().__init__(width, height, x, y, id)

    def __str__(self):
        name = __class__.__name__
        size = self.width
        return f"[{name}] ({self.id}) {self.x}/{self.y} - {size}"

    @property
    def size(self):
        """Size setter."""
        return self.width

    @size.setter
    def size(self, value):
        """size setter function."""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be > 0")
        self.width = self.height = value

    def update(self, *args, **kwargs):
        """Function to update attributes acourding to args given"""
        if args and len(args) > 0:
            attrib = ['id', 'size', 'x', 'y']
            for i in range(len(args)):
                setattr(self, attrib[i], args[i])
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """This function returns dictionary representation of the square."""
        dic = {
                'id': self.id,
                'size': self.size,
                'x': self.x,
                'y': self.y
                }
        return dic
