#!/usr/bin/python3


import unittest
import os
import sys
#import pep8
from models.base import Base


class BaseTestCase(unittest.TestCase):

    def test_base(self):
        self.assertIsNone(Base.___doc__)
    
    #def test_style_base(self):
     #   """Test for PEP8"""
      #  style = pep8.StyleGuide(quiet=True)


if __name__ == "__main__":
    unittest.main()
