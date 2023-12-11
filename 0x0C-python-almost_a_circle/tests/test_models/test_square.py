#!/usr/bin/python3
"""Test case for the Square class."""
from models.square import Square
import unittest


class TestSquare(unittest.TestCase):
    """CLass TestSqaure defined here."""
    def test_for_id(self):
        a = Square(2, 4)
        self.assertEqual(a.id, 1)

    def test_width_value(self):
        a = Square(2, 5)
        self.assertEqual(a.width, 2)

    def test_height_value(self):
        a = Square(3, 6)
        self.assertEqual(a.height, 3)

    """Testing size setter module."""
    def Test_setter(self):
        a = Square(5)
        a.size = 18
        self.assertEqual(a.size, 18)

    """Testing update() method."""
    def test_id_value(self):
        a = Square(2, 3, 4, 3)
        a.update(12)
        self.assertEqual(a.id, 12)

    def test_size_value(self):
        a = Square(1, 3, 4, 6)
        a.update(12, 21)
        self.assertEqual(a.size, 21)

    def test_x_value(self):
        a = Square(1, 3, 4, 6)
        a.update(12, 21, 23)
        self.assertEqual(a.x, 23)

    def test_y_value(self):
        a = Square(1, 3, 4, 6)
        a.update(12, 21, 23, 32)
        self.assertEqual(a.y, 32)

    """Testing to_dictionary() function."""
    def test_to_dictionary(self):
        a = Square(1, 2)
        b = Square(3, 4)
        d = a.to_dictionary()
        b.update(**d)
        self.assertEqual(b.size, 1)


if __name__ == '__main__':
    unittest.main()
