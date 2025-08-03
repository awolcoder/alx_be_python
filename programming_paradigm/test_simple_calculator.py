import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """Unit tests for the SimpleCalculator class."""

    def setUp(self):
        """
        Create a new SimpleCalculator instance before each test method.
        This ensures each test runs with a fresh calculator.
        """
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the add method with various inputs."""
        self.assertEqual(self.calc.add(2, 3), 5)          # Positive integers
        self.assertEqual(self.calc.add(-1, 1), 0)         # Negative and positive
        self.assertEqual(self.calc.add(0, 0), 0)          # Zero addition
        self.assertAlmostEqual(self.calc.add(2.5, 3.1), 5.6)  # Floating point numbers

    def test_subtraction(self):
        """Test the subtract method with various inputs."""
        self.assertEqual(self.calc.subtract(5, 3), 2)     # Positive integers
        self.assertEqual(self.calc.subtract(0, 0), 0)     # Zero subtraction
        self.assertEqual(self.calc.subtract(-1, -1), 0)   # Negative numbers
        self.assertAlmostEqual(self.calc.subtract(2.5, 1.2), 1.3)  # Floating point numbers

    def test_multiplication(self):
        """Test the multiply method with various inputs."""
        self.assertEqual(self.calc.multiply(3, 4), 12)    # Positive integers
        self.assertEqual(self.calc.multiply(0, 100), 0)   # Multiplying by zero
        self.assertEqual(self.calc.multiply(-2, 3), -6)   # Negative times positive
        self.assertAlmostEqual(self.calc.multiply(2.5, 4), 10.0)  # Floating point multiplication

    def test_division(self):
        """Test the divide method including division by zero."""
        self.assertEqual(self.calc.divide(10, 2), 5)      # Normal division
        self.assertEqual(self.calc.divide(3, 2), 1.5)     # Floating point division
        self.assertIsNone(self.calc.divide(5, 0))         # Division by zero returns None
        self.assertEqual(self.calc.divide(-6, 3), -2)     # Negative numerator

if __name__ == '__main__':
    unittest.main()
