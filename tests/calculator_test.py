"""Testing the Calculator"""
import unittest

from calculator.main import Calculator


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_calculator_result(self):
        """testing calculator result is 0"""
        calc = Calculator()
        assert calc.result == 0

    def test_calculator_add(self):
        """Testing the Add function of the calculator"""
        #Arrange by instantiating the calc class
        calc = Calculator()
        #Act by calling the method to be tested
        calc.add_number(4)
        #Assert that the results are correct
        assert calc.result == 4

    def test_calculator_get_result(self):
        """Testing the Get result method of the calculator"""
        calc = Calculator()
        calc.add_number(1)
        assert calc.get_result() == 1

    def test_calculator_subtract(self):
        """Testing the subtract method of the calculator"""
        calc = Calculator()
        calc.subtract_number(1)
        assert calc.get_result() == -1

    def test_calculator_multiplication(self):
        """ testing multiplication"""
        calc = Calculator()
        calc.multiply_numbers(1, 2)
        assert calc.get_result() == 2

    def test_calculator_division(self):
        """ testing division"""
        calc = Calculator()
        calc.divide_numbers(1, 2)
        assert calc.get_result() == 0.5

    def test_calculator_division_by_zero(self):
        """ testing dividing by 0"""
        calc = Calculator()
        self.assertRaises(ZeroDivisionError, calc.divide_numbers(1, 0))


if __name__ == '__main__':
    unittest.main()
