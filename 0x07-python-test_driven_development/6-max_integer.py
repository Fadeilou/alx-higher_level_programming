#!/usr/bin/python3
"""Unittest for max_integer([...])
"""
import unittest
from max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    def test_regular_list(self):
        """Test with a regular list"""
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2]), 4)

    def test_empty_list(self):
        """Test with an empty list"""
        self.assertIsNone(max_integer([]))

    def test_negative_values(self):
        """Test with a list containing negative values"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-4, -2, -3, -1]), -1)

    def test_float_values(self):
        """Test with a list containing float values"""
        self.assertEqual(max_integer([1.5, 2.5, 3.5, 4.5]), 4.5)
        self.assertEqual(max_integer([1.5, 3.5, 4.5, 2.5]), 4.5)

    def test_duplicate_values(self):
        """Test with a list containing duplicate values"""
        self.assertEqual(max_integer([4, 4, 4, 4]), 4)
        self.assertEqual(max_integer([1, 1, 1, 1]), 1)

    def test_mixed_values(self):
        """Test with a list containing mixed types"""
        self.assertEqual(max_integer([1, 2, "3", 4]), 4)
        self.assertEqual(max_integer([1, 3, 4.5, 2]), 4.5)

if __name__ == '__main__':
    unittest.main()
