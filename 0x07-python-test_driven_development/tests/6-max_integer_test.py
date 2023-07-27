#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer

list_1 = [5, 4, 10, 78, 45]
empty_list = []

class TestMax_integer(unittest.TestCase):
    
    def setUp(self):
        """Setting upof the list"""
        self.list_1 = list_1
        self.list_empty = empty_list
    
    def test_max_integer(self):
        """Checking for max integer"""
        self.assertEqual(max_integer(self.list_1), 78)
    
    def test_empty_list(self):
        """Checking for empty list"""
        self.assertIsNone(max_integer(self.list_empty), msg="None")

if __name__ == "__main__":
    unittest.main()
