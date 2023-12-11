#!/usr/bin/python3
"""Test suit for the Base class."""
from models.base import Base
from models.rectangle import Rectangle
import unittest


class TestBase(unittest.TestCase):
    """The TestBase class is defined here."""
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_for_normal_case(self):
        a = Base()
        self.assertEqual(a.id, 1)

    def test_for_two_instances(self):
        a = Base()
        a1 = Base()
        a2 = Base()
        self.assertEqual(a1.id, 3)

    def test_for_id_given(self):
        a = Base(12)
        self.assertEqual(a.id, 12)

    def test_mixed(self):
        a1 = Base()
        a2 = Base()
        a3 = Base(23)
        self.assertEqual(a3.id, 23)

    """Testing to_json_string() function"""
    def test_to_json_string(self):
        a = Rectangle(1, 3)
        dl = a.to_dictionary()
        json_s = Base.to_json_string([dl])
        self.assertEqual(type(json_s), str)

    """TEsting saave_to_file() function."""


if __name__ == '__main__':
    unittest.main()
