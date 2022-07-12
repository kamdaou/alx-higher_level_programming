#!/usr/bin/python3

import unittest
from models.base import Base

"""Unit test of Base class"""


class TestBaseClass(unittest.TestCase):
    """
    Creates test case for Base class
    """

    def test_baseWithId(self):
        """
        Tests if creating an instance of base class with an id gives the right value.
        """
        base = Base(2)
        self.assertEqual(base.id, 2)

    def test_baseWithoutId(self):
        """
        Tests if creating an instance of base class without an id gives the right value.
        """
        base = Base()
        self.assertEqual(base.id, 1)


if __name__ == '__main__':
    unittest.main()
