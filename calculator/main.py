""" This is the increment function"""


class Calculator:
    """ This is the Calculator class"""
    result = 0

    def get_result(self):
        """ Get Result of Calculation"""
        return self.result

    def add_number(self, value_a):
        """ adds number to result"""
        self.result = self.result + value_a
        return self.result

    def subtract_number(self, value_a):
        """ subtract number from result"""
        self.result = self.result - value_a
        return self.result

    def multiply_numbers(self, value_a, value_b):
        """ multiply two numbers and get result"""
        self.result = value_a * value_b
        return self.result

    def divide_numbers(self, value_a, value_b):
        """With two real values, divide value a by value b (a / b)"""
        try:
            self.result = value_a / value_b
            return self.result
        except ZeroDivisionError:
            raise ZeroDivisionError("ZeroDivisionError: integer division or modulo by zero")
            return None
