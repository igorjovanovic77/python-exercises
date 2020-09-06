
import unittest

def add(a,b):
    return a+b




class TestCalc(unittest.TestCase):

    def test_001_1plus2eq3(self):
        self.assertEqual(3, add(1, 2))

    def test_002_0plus3(self):
        self.assertEqual(3, add(0, 3))

