"""Testing the Calculator"""
from calculator.main import Calculator

def test_calculator_result():
    """testing calculator result is 0"""
    calc = Calculator()
    assert calc.result == 0

def test_calculator_add():
    """Testing the Add function of the calculator"""
    #Arrange by instantiating the calc class
    calc = Calculator()
    #Act by calling the method to be tested
    calc.add_number(4)
    #Assert that the results are correct
    assert calc.result == 4

def test_calculator_get_result():
    """Testing the Get result method of the calculator"""
    calc = Calculator()
    calc.add_number(1)
    assert calc.get_result() == 1

def test_calculator_subtract():
    """Testing the subtract method of the calculator"""
    calc = Calculator()
    calc.subtract_number(1)
    assert calc.get_result() == -1

def test_calculator_multiplication():
    """ testing multiplication"""
    calc = Calculator()
    calc.multiply_numbers(1, 2)
    assert calc.get_result() == 2

def test_calculator_division():
    """ testing multiplication"""
    calc = Calculator()
    calc.divide_numbers(1, 2)
    assert calc.get_result() == 2

def test_calculator_divide_by_zero():
    """ testing multiplication"""
    calc = Calculator()
    assert calc.divide(1, 0) is None
