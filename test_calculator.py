import unittest
import pytest
from calculator import calculate  # file name and my function calculate to be tested

class TestCalculate(unittest.TestCase):

    def test_addition(self):
        result = calculate("5+3")
        self.assertEqual(result, 8)

    def test_subtraction(self):
        result = calculate("10-4")
        self.assertEqual(result, 6)

    def test_multiplication(self):
        result = calculate("3*4")
        self.assertEqual(result, 12)

    def test_division(self):
        result = calculate("8/2")
        self.assertEqual(result, 4)

    def test_exponentiation(self):
        result = calculate("2^3")
        self.assertEqual(result, 8)

    def test_complex_expression(self):
        result = calculate("(5+3)*2")
        self.assertEqual(result, 16)

    def test_complex_expression(self):
        result = calculate("(9+3)*3")
        self.assertEqual(result, 26) # check should fail as 26 is incorrect should be 36 

    def test_invalid_input(self):
        with self.assertRaises(Exception):
            calculate("5/0")

if __name__ == "__main__":
    unittest.main()