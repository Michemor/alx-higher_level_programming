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
        b = Base()
        self.assertIsNotNone(b)
    
    def test_id(self):
        """
        tests how ids are created
        """
        b1 = Base()
        self.assertEqual(b1.id, 2)

        b2 = Base()
        self.assertEqual(b2.id, 3)

        for i in range(2):
            b = Base()
            
        b3 = Base()
        self.assertEqual(b3.id, 6)

        b4 = Base(45)
        self.assertEqual(b4.id, 45)

        # check for the number of objects created so far
