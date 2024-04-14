import unittest
from models.base import Base


class TestBase(unittest.TestCase):

    def test_id_incrementation(self):
        b1 = Base()
        b2 = Base()
        b3 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)

    def test_id_given_value(self):
        b4 = Base(10)
        self.assertEqual(b4.id, 10)

    def test_id_not_given_value(self):
        b5 = Base()
        self.assertEqual(b5.id, 4)
