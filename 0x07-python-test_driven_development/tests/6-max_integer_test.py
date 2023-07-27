#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer

list_1 = [5, 4, 10, 78, 45]
list_2 = [13]
empty_list = []
negative_list = [-5, -30, -3]
negative_list_2 = [-4]
max_at_beginning = [4, 3, 2, 1]

class TestMax_integer(unittest.TestCase):
    
    def setUp(self):
        """Setting upof the list"""
        self.list_1 = list_1
        self.list_empty = empty_list
        self.one_list = list_2
        self.list_negative = negative_list
        self.list_2_negative = negative_list_2
        self.list_max_begining = max_at_beginning

    def test_max_integer(self):
        """Checking for max integer"""
        self.assertEqual(max_integer(self.list_1), 78)
    
    def test_empty_list(self):
        """Checking for empty list"""
        self.assertIsNone(max_integer(self.list_empty), msg="None")
    
    def test_max_integer_negative(self):
            """Checking for max integer negative numbers"""
            self.assertEqual(max_integer(self.list_negative), -3)
    
    def test_max_integer_one_negative(self):
            """Checking for max integer in a list with one element"""
            self.assertEqual(max_integer(self.list_2_negative), -4)
    
    def test_max_integer_one_integer(self):
            """Checking for max integer"""
            self.assertEqual(max_integer(self.one_list), 13)
    
    def test_max_at_begginning(self):
            """Testing a list with a beginning max value."""
            self.assertEqual(max_integer(self.list_max_begining), 4)

if __name__ == "__main__":
    unittest.main()
