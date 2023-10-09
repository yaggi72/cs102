import unittest
import sys
from ../..src.lab1.calculator import Calculator
class TestCalculator(unittest.TestCase):
    def test_Calculator(self):
        self.assertEqual(Calculator(5, 2, '+'), 7)
        self.assertEqual(Calculator(5.0, 2, '-'), 3.0)
        self.assertEqual(Calculator(5, 2.0, '*'), 10)
        self.assertEqual(Calculator(5, 2, '/'), 2.5)
        self.assertEqual(Calculator(5, 2, '123'), 'Вы ошиблись во вводе')
        self.assertEqual(Calculator(5, 'asds54sdf', '*'), 'Вы ошиблись во вводе')
