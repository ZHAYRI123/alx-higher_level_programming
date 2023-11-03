#!/usr/bin/python3
"""Unittest of the max of a list"""


import unittest
max_integer = __import__(6-max_integer).max_integer

class TestMaxInteger(unittest.TestCase):
    """test max of a list"""
    def test_empty(self):
        """if list is empty"""
        my_list = []
        self.assertEqual(max_integer(my_list), None)
    def test_one(self):
        """list has one item"""
        my_list = [1]
        self.assertEqual(max_integer(my_list), 1)
    def test_ordored(self):
        """list is ordored"""
        my_list = [4, 3, 2, 1]
        self.assertEqual(max_integer(my_list), 4)
    def test_inverse(self):
        """list is inverse"""
        my_list = [4, 5, 6, 7]
        self.assertEqual(max_integer(my_list), 7)
    def test_not_in_order(self):
        """list not in order"""
        my_list = [5, 1, 4, 7]
        self.assertEqual(max_integer(my_list), 7)
    def test_negative(self):
        """negative value"""
        my_list = [-1, -2, -3, -4]
        self.assertEqual(max_integer(my_list), -1)
    def test_negpos(self):
        """list has negative & positive item"""
        my_list = [-1, 2, -3, 4]
        self.assertEqual(max_integer(my_list), 4)
