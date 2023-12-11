#!/usr/bin/python3
"""Test suit for Rectangle class."""
from models.rectangle import Rectangle
from models.base import Base
import unittest


class TestRectangle(unittest.TestCase):
    """Definition of the TestRectangle class."""

    def setUp(self):
        Base.reset_nb_objects()

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



    """Testing where error exceptions are thrown."""



    """Testing area of rectangle."""
    def test_for_only_w_and_h_given(self):
        a = Rectangle(2, 3)
        self.assertEqual(a.area(), 6)

    def test_for_three_values_given(self):
        a = Rectangle(3, 5, 7)
        self.assertEqual(a.area(), 15)

    def test_for_all_values_given(self):
        a = Rectangle(1, 3, 4, 7, 8)
        self.assertEqual(a.area(), 3)



    """Testing display() method."""
    def test_4_and_1(self):
        a = Rectangle(4, 1)
        self.assertEqual(a.display(), None)



    """Testing special methon str."""
    def test_str_representation(self):
        rectangle = Rectangle(10, 2, 5, 10)
        expected_string = "[Rectangle] (1) 5/10 - 10/2"
        self.assertEqual(str(rectangle), expected_string)



    """Tests for display that handles x and y."""




    """Testing update() method with args and kwargs."""
    def test_update(self):
        a = Rectangle(2, 2, 2, 2, 2)
        self.assertEqual(a.area(), 4)

    def test_update1(self):
        a = Rectangle(89, 78)
        a.update(145)
        self.assertEqual(a.id, 145)

    def test_kwargs(self):
        a = Rectangle(1, 2, 3, 5, 6)
        a.update(width = 6, y = 3, height = 89)
        self.assertEqual(a.height, 89)



    """Testing to_dictionary function."""
    def test_to_dictionary(self):
        a = Rectangle(2, 1)
        d = a.to_dictionary()
        b = Rectangle(4, 6)
        b.update(**d)
        self.assertEqual(b.width, 2)



if __name__ == '__main__':
    unittest.main()
