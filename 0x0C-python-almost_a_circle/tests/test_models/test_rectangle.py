#!/usr/bin/python3


from turtle import width
import unittest
import os
import sys
import pep8
from models.rectangle import Rectangle


class TestRectangleCase(unittest.TestCase):

    def setUp(self):
        # Set up any necesssary objects or variabl
        pass

    def test_base_check(self):
        self.assertIsNotNone(Rectangle.__doc__)
        self.assertIsNotNone(width.__doc__)

    def test_base_pep8(self):
        """Test if Rectangle code conforms to PEP8 style guide"""
        style = pep8.StyleGuide(quiet=True)
        # r = style.check_files(['tests/tests_models/test_base.py'])
        # self.assertEqual(r.total_errors, 0,
        # "PEP8 style errors: %d" % r.total_errors)
        result = style.check_files(['models/rectangle.py'])
        self.assertEqual(result.total_errors, 0,
                         "PEP8 style errors: %d" % result.total_errors)

    def test_documentation(self):
        """Test to see if documentation is correct"""
        self.assertTrue(hasattr(Rectangle, "__init__"))

    def test_base_init(self):
        """Test if rectangle class initialises correctly"""
        rec = Rectangle()
        self.assertIsInstance(rec, Rectangle)
        # self.assertEqual(b.id, 1)


if __name__ == "__main__":
    unittest.main()
