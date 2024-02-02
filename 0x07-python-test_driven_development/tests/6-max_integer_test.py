#!/usr/bin/python3

def max_integer(lst):
    if not lst:
        return None
    return max(lst)


import unittest
from max_integer import max_integer

class TestMaxInteger(unittest.TestCase):
    def test_max_in_list(self):
        self.assertEqual(max_integer([1, 3, 2, 4]), 4)

    def test_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_negative_numbers(self):
        self.assertEqual(max_integer([-1, -3, -2, -4]), -1)

    def test_duplicate_numbers(self):
        self.assertEqual(max_integer([5, 5, 5, 5]), 5)

    def test_float_numbers(self):
        self.assertEqual(max_integer([1.5, 3.7, 2.2, 4.1]), 4.1)

    def test_mixed_numbers(self):
        self.assertEqual(max_integer([1, -3, 2.2, -4.1]), 2.2)

if __name__ == '__main__':
    unittest.main()
