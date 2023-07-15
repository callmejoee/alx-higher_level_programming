#!/usr/bin/python3
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    
    def test_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 5, 3, 4]), 5)
        self.assertEqual(max_integer([1, 2, 123, 1222, 1222, 3, 4]), 1222)
        self.assertEqual(max_integer([-1, -2, 3, 4]), 4)
        self.assertEqual(max_integer([-1, -2, -3, -4]), -1)
        self.assertEqual(max_integer([-41, -122, 0, -3, -4]), 0)
        self.assertEqual(max_integer([1]), 1)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer(), None)
        
    def test_string(self):
        self.assertEqual(max_integer(["banana", "apple"]), "banana")
        self.assertEqual(max_integer(["banana", "apple", "cat"]), "cat")
        self.assertEqual(max_integer(["banana", "Apple"]), "banana")
        self.assertEqual(max_integer(["banana", "apple", "Cat"]), "banana")

if __name__ == "__main__":
    unittest.main()
