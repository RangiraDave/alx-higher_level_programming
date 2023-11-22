#!/usr/bin/python3

"""Difining the Square class."""


class Square:
    """
    The Square class represents a geometric square.
    """
    def __init__(self, _size=0):
        """
        Initializes a new instance of the Square class.

        Args:
            _size (int): The size of the square.
        """
        if type(_size) is not int:
            raise TypeError("size must be an integer")
        if _size < 0:
            raise ValueError("size must be >= 0")

        self._Square__size = _size
