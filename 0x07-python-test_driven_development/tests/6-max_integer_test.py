import unittest

class TestMaxInteger(unittest.TestCase):
    
    def test_integer(self):
        self.assertEqual(print(max_integer([1, 2, 3, 4])), 4)
        self.assertEqual(print(max_integer([1, 5, 3, 4])), 5)
        self.assertEqual(print(max_integer([1, 2, 123, 1222, 1222, 3, 4])), 1222)
        self.assertEqual(print(max_integer([-1, -2, 3, 4])), 4)
        self.assertEqual(print(max_integer([-1, -2, -3, -4])), -1)
        self.assertEqual(print(max_integer([-41, -122, 0, -3, -4])), 0)
        self.assertEqual(print(max_integer([1])), 1)
        self.assertEqual(print(max_integer([]))
        self.assertEqual(print(max_integer()), None)
        
    def test_string(self):
        self.assertEqual(print(max_integer(["banana", "apple"])), banana)
        self.assertEqual(print(max_integer(["banana", "apple", "cat"])), cat)
        self.assertEqual(print(max_integer(["banana", "Apple"])), banana)
        self.assertEqual(print(max_integer(["banana", "apple", "Cat"])), banana)
