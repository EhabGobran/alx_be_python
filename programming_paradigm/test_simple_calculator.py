import unittest
from simple_calculator import SimpleCalculator

class TestSimpleClass(unittest.TestCase):
    def setUp(self):
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(6,3),9)
        self.assertEqual(self.calc.add(6,0),6)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(6,3),18)
        self.assertEqual(self.calc.multiply(6,0),0)

    def test_division(self):
        self.assertEqual(self.calc.divide(6,3),2)
        self.assertEqual(self.calc.divide(6,0),None)

    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(6,3),3)
        self.assertEqual(self.calc.subtract(6,0),6)

