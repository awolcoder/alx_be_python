class Calculator:
    """
    A simple calculator demonstrating the use of
    static methods and class methods in Python.
    """

    # Class attribute
    calculation_type = "Arithmetic Operations"

    @staticmethod
    def add(a, b):
        """
        Static method to return the sum of two numbers.

        Args:
            a (float or int): First number.
            b (float or int): Second number.

        Returns:
            float or int: The sum of a and b.
        """
        return a + b

    @classmethod
    def multiply(cls, a, b):
        """
        Class method to return the product of two numbers.
        Prints the calculation type before performing multiplication.

        Args:
            a (float or int): First number.
            b (float or int): Second number.

        Returns:
            float or int: The product of a and b.
        """
        print(f"Calculation type: {cls.calculation_type}")
        return a * b
