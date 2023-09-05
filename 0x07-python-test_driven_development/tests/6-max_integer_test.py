#!/usr/bin/python3
import unittest

max_integer = __import__('6-max_integer').max_integer

class Max_int_test_suit(unittest.TestCase):
    def test_list(self):
        self.assertEqual(max_integer([10, 11, 34, 234, 1212]), 1212)

    def test_neg_num(self):
        self.assertEqual(max_integer([-132, -32, -3, -309, -7, -133]), -3)

    def test_empty(self):
        self.assertEqual(max_integer(), None)

    def test_not_list(self):
        with self.assertRaises(TypeError):
            max_integer(10)

if __name__ == "__main__":
    unittest.main()
