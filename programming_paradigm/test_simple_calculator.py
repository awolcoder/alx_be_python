import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """Unit tests for the SimpleCalculator class."""

    def setUp(self):
        """Set up a SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    # --- ADDITION TESTS ---
    def test_addition_positive_numbers(self):
        """Test addition with positive integers."""
        self.assertEqual(self.calc.add(2, 3), 5)

    def test_addition_negative_numbers(self):
        """Test addition with negative integers."""
        self.assertEqual(self.calc.add(-5, -7), -12)

    def test_addition_mixed_numbers(self):
        """Test addition with positive and negative integers."""
        self.assertEqual(self.calc.add(-3, 7), 4)

    def test_addition_floats(self):
        """Test addition with floating-point numbers."""
        self.assertAlmostEqual(self.calc.add(2.5, 3.1), 5.6)

    # --- SUBTRACTION TESTS ---
    def test_subtraction_positive_numbers(self):
        """Test subtraction with positive integers."""
        self.assertEqual(self.calc.subtract(10, 3), 7)

    def test_subtraction_negative_numbers(self):
        """Test subtraction with negative integers."""
        self.assertEqual(self.calc.subtract(-5, -3), -2)

    def test_subtraction_mixed_numbers(self):
        """Test subtraction with positive and negative integers."""
        self.assertEqual(self.calc.subtract(5, -2), 7)

    def test_subtraction_floats(self):
        """Test subtraction with floating-point numbers."""
        self.assertAlmostEqual(self.calc.subtract(5.5, 2.2), 3.3)

    # --- MULTIPLICATION TESTS ---
    def test_multiplication_positive_numbers(self):
        """Test multiplication with positive integers."""
        self.assertEqual(self.calc.multiply(4, 3), 12)

    def test_multiplication_negative_numbers(self):
        """Test multiplication with negative integers."""
        self.assertEqual(self.calc.multiply(-4, -3), 12)

    def test_multiplication_mixed_numbers(self):
        """Test multiplication with positive and negative integers."""
        self.assertEqual(self.calc.multiply(-4, 3), -12)

    def test_multiplication_with_zero(self):
        """Test multiplication with zero."""
        self.assertEqual(self.calc.multiply(0, 100), 0)

    def test_multiplication_floats(self):
        """Test multiplication with floating-point numbers."""
        self.assertAlmostEqual(self.calc.multiply(2.5, 4.0), 10.0)

    # --- DIVISION TESTS ---
    def test_division_positive_numbers(self):
        """Test division with positive integers."""
        self.assertEqual(self.calc.divide(10, 2), 5)

    def test_division_negative_numbers(self):
        """Test division with negative integers."""
        self.assertEqual(self.calc.divide(-10, -2), 5)

    def test_division_mixed_numbers(self):
        """Test division with positive and negative integers."""
        self.assertEqual(self.calc.divide(-10, 2), -5)

    def test_division_floats(self):
        """Test division with floating-point numbers."""
        self.assertAlmostEqual(self.calc.divide(7.5, 2.5), 3.0)

    def test_division_by_zero(self):
        """Test division by zero returns None."""
        self.assertIsNone(self.calc.divide(10, 0))

if __name__ == "__main__":
    unittest.main()
