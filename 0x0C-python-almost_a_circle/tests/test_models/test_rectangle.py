#!/usr/bin/python3
"""Test suit for Rectangle class."""
from models.rectangle import Rectangle
import unittest


class TestRectangle(unittest.TestCase):
    """Definition of the TestRectangle class."""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_for_normal_case(self):
        a = Rectangle(2, 4, 5, 6)
        self.assertEqual(a.id, 1)

    def test_when_id_is_given(self):
        a = Rectangle(1, 2, 4, 5, 71)
        self.assertEqual(a.id, 71)

    def test_for_width(self):
        a = Rectangle(2, 4)
        self.assertEqual(a.width, 2)

    def test_for_x(self):
        a = Rectangle(3, 5, 6, 7)
        self.assertEqual(a.x, 6)

if __name__ == '__main__':
    unittest.main()
