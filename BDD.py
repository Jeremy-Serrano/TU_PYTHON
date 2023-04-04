import unittest
from main import addition, soustraction, multiplication, division

class TestOperations(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(addition(2, 3), 5)
        self.assertEqual(addition(0, 0), 0)
        self.assertEqual(addition(-1, 1), 0)

    def test_soustraction(self):
        self.assertEqual(soustraction(5, 2), 3)
        self.assertEqual(soustraction(0, 0), 0)
        self.assertEqual(soustraction(-1, 1), -2)

    def test_multiplication(self):
        self.assertEqual(multiplication(2, 3), 6)
        self.assertEqual(multiplication(0, 0), 0)
        self.assertEqual(multiplication(-1, 1), -1)
        self.assertEqual(multiplication(2.5, 4), 10)
        self.assertEqual(multiplication(2, 4.5), 9)
        self.assertEqual(multiplication(2.5, 4.5), 11.25)
        self.assertEqual(multiplication(2, (3 + 4)), 14)

    def test_division(self):
        self.assertEqual(division(6, 3), 2)
        self.assertEqual(division(0, 5), 0)
        with self.assertRaises(ValueError):
            division(1, 0)
        self.assertEqual(division(10, 4), 2.5)
        self.assertEqual(division(12.5, 2.5), 5)
        self.assertEqual(division(10, (2 + 2)), 2.5)


if __name__ == '__main__':
    unittest.main()
