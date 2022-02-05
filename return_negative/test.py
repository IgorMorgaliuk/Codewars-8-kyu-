import unittest 
from solution1 import make_negative

class TestMakeNegative(unittest.TestCase):
    def test_make_negative_int(self):
        self.assertEqual(make_negative(5), -5)
        self.assertEqual(make_negative(-5), -5)
        self.assertEqual(make_negative(0), 0)

    def test_make_negative_float(self):
        self.assertEqual(make_negative(5.3), -5.3)
        self.assertEqual(make_negative(-5.7), -5.7)
        

if __name__ == '__main__':
    unittest.main()