import unittest

from src.lab1.calculator import Calculator

class Test(unittest.TestCase):
    def test_Calculator(self):
        assert Calculator(5, 2, '+') == 7
        assert Calculator(5.0, 2, '-') == 3.0
        assert Calculator(5, 2.0, '*') == 10
        assert Calculator(5, 2, '/') == 2.5
        assert Calculator(5, 2, '123') == 'Ошибка ввода'
        assert Calculator(5, 'asds54sdf', '*') == 'Ошибка ввода'
