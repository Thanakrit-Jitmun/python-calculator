import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:
    def test_add_1(self):
        self.assertEqual(self.calc.add(4, 5), 9)

    def test_add_2(self):
        self.assertEqual(self.calc.add(20, 2), 22)
    
    def test_subtract_1(self):
        self.assertEqual(self.calc.subtract(99, 77), 22)

    def test_subtract_2(self):
        self.assertEqual(self.calc.subtract(55, 5), 50)

    def test_multiply_1(self):
        self.assertEqual(self.calc.multiply(100, 5), 500)

    def test_multiply_2(self):
        self.assertEqual(self.calc.multiply(1000, 10), 10000)

    def test_divide_1(self):
        self.assertEqual(self.calc.divide(2000, 5), 400)

    def test_divide_2(self):
        self.assertEqual(self.calc.divide(1000, 10), 100)

    def test_modulo_1(self):
        self.assertEqual(self.calc.modulo(2000, 2), 0)

    def test_modulo_2(self):
        self.assertEqual(self.calc.modulo(10001, 2), 1)
    

if __name__ == '__main__':
    unittest.main()