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

    def test_string(self):
        """Test a string"""
        self.assertEqual(max_integer("hello"), 'o')
        self.assertEqual(max_integer("world"), 'r')

    def test_max_at_end(self):
        """Test for max at the end"""
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)

    def test_max_at_beginning(self):
        """Test for max at the beginning"""
        self.assertEqual(max_integer([5, 1, 2, 3, 4]), 5)

    def test_max_in_middle(self):
        """Test for max in the middle"""
        self.assertEqual(max_integer([1, 2, 5, 3, 4]), 5)

    def test_one_negative_number(self):
        """Test for one negative number in the list"""
        self.assertEqual(max_integer([-1]), -1)

    def test_only_negative_numbers(self):
        """Test for only negative numbers in the list"""
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)

    def test_list_of_one_element(self):
        """Test for list of one element"""
        self.assertEqual(max_integer([42]), 42)

if __name__ == '__main__':
    unittest.main()
