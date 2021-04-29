from calc import *
import unittest


class TestStringMethods(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(add(5,10), 15)
        self.assertEqual(add(5,4), 9)
        self.assertEqual(add(25,4), 20)

    def test_subtraction(self):
        self.assertEqual(sub(5,10), -5)
        self.assertEqual(sub(5,4), 1)

    def test_multiplication(self):
        self.assertEqual(mult(5,10), 50)
        self.assertEqual(mult(5,4), 20)
        self.assertEqual(mult(5,0), 0)    

    def test_division(self):
        self.assertEqual(div(10,2), 5)
        self.assertEqual(div(50,5), 10)
        self.assertEqual(div(50,5), -10)

if __name__ == "__main__":
    unittest.main()