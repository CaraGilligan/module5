import unittest

from calculator import calculator

class testoperation(unittest.TestCase):
    def setUp(self):
        self.calc = calculator(8,2)


    def test_sum(self):
        self.assertEqual(self.calc.get_sum(), 10, "The answer is not correct")

    def test_sub(self):
        calc = calculator(8,2)
        self.assertEqual(self.calc.get_subtract(), 8, "The answer is not correct")

    def test_mult(self):
        calc = calculator(8,2)
        self.assertEqual(self.calc.get_multiply(), 80, "The answer is not correct")

    def test_div(self):
        calc = calculator(8,2)
        self.assertEqual(self.calc.get_divide(), 4, "The answer is not correct")

    if __name__ == "__main__" : 
        unittest.main()