import unittest
from main import calculer


class TestCalculatrice(unittest.TestCase):

    def test_calculer_expression_complexe(self):
        self.assertEqual(calculer("(1+2)*(3-1)/2"), 3.0)

    def test_calculer_division_par_zero(self):
        with self.assertRaises(ValueError):
            calculer("1/0")

    def test_calculer_expression_invalide(self):
        with self.assertRaises(SyntaxError):
            calculer("1 ++ 2")

if __name__ == '__main__':
    unittest.main()
