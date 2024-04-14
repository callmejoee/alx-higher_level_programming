import unittest

from models.rectangle import Rectangle

class TestRectangle(unittest.TestCase):

    def test_attributes(self):
        r = Rectangle(10, 20, 5, 10, 1)
        self.assertEqual(r.width, 10)
        self.assertEqual(r.height, 20)
        self.assertEqual(r.x, 5)
        self.assertEqual(r.y, 10)
        self.assertEqual(r.id, 1)
