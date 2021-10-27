"""Testing the Calculator"""
import unittest

from calculator.main import Calculator


class MyTestCase(unittest.TestCase):
    """Class to test calculator. Mainly made for divide function"""
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_calculator_result(self):
        """testing calculator result is 0"""
        self.calculator = Calculator()
        assert self.calculator.result == 0

    def test_calculator_add(self):
        """Testing the Add function of the calculator"""
        #Arrange by instantiating the calc class
        self.calculator = Calculator()
        #Act by calling the method to be tested
        self.calculator.add_number(4)
        #Assert that the results are correct
        assert self.calculator.result == 4

    def test_calculator_get_result(self):
        """Testing the Get result method of the calculator"""
        self.calculator = Calculator()
        self.calculator.add_number(1)
        assert self.calculator.get_result() == 1

    def test_calculator_subtract(self):
        """Testing the subtract method of the calculator"""
        self.calculator = Calculator()
        self.calculator.subtract_number(1)
        assert self.calculator.get_result() == -1

    def test_calculator_multiplication(self):
        """ testing multiplication"""
        self.calculator = Calculator()
        self.calculator.multiply_numbers(1, 2)
        assert self.calculator.get_result() == 2

    def test_calculator_division(self):
        """ testing division"""
        self.calculator = Calculator()
        self.calculator.divide_numbers(1, 2)
        assert self.calculator.get_result() == 0.5

    def test_calculator_division_by_zero(self):
        """ testing dividing by 0"""
        self.calculator = Calculator()
        with self.assertRaises(ZeroDivisionError):
            self.calculator.divide_numbers(1, 0)


if __name__ == '__main__':
    unittest.main()
