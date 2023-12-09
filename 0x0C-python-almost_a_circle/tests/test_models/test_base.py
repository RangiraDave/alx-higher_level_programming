#!/usr/bin/python3
"""Test suit for the Base class."""
from models.base import Base
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



if __name__ == '__main__':
    unittest.main()
