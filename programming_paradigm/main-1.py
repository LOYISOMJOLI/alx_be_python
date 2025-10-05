import unittest
from test_simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        # Add more assertions to thoroughly test the add method.

    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(6, 4), 2)
        self.assertEqual(self.calc.subtract(-5, 1), 4)
        self.assertEqual(self.calc.subtract(7,8), 2)

    def test_multiplication(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(5, 3), 15)
        self.assertEqual(self.calc.multiply(-1, 1), -1)


    def test_divide(self):
        """Test the division method."""
        self.assertEqual(self.calc.divide(6, 3), 1)
        self.assertEqual(self.calc.divide(30, 5), 6)
# Remember to write additional test methods for subtract, multiply, and divide.

if __name__ == "___main__":
    unittest.main()
