#!/usr/bin/python3
""" test class for rectangle class """
from models.base import Base
from models.rectangle import Rectangle
import unittest


class TestRectangle(unittest.TestCase):
    """
    a set of test cases for the functionality of rectangle class
    """

    def test_create_object(self):
        """
        tests the creation of an object
        """
        rec = Rectangle(5, 10, 3, 4, 12)
        self.assertIsNotNone(rec)
        self.assertEqual(rec.width, 5)
        self.assertEqual(rec.height, 10)
        self.assertEqual(rec.x, 3)
        self.assertEqual(rec.y, 4)

    def test_width(self):
        """
        test for the dimensions for the width
        """
        rec = Rectangle(10, 14, 2, 5, 89)
        self.assertEqual(rec.width, 10)
        self.assertEqual(rec.height, 14)

    def test_area(self):
        """
        test case for instantiation of rectangle area
        """
        r1 = Rectangle(4, 12)
        self.assertEqual(r1.area(), 48) 
