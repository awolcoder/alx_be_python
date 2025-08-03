def safe_divide(numerator, denominator):
    """
    Safely performs division between numerator and denominator.

    Args:
        numerator (str): The numerator (string from CLI).
        denominator (str): The denominator (string from CLI).

    Returns:
        str: Result of division or an error message.
    """
    try:
        # Attempt to convert inputs to floats
        num = float(numerator)
        den = float(denominator)

        # Attempt division
        result = num / den
        return f"The result of the division is {result}"

    except ValueError:
        # Handles non-numeric input
        return "Error: Please enter numeric values only."
    except ZeroDivisionError:
        # Handles division by zero
        return "Error: Cannot divide by zero."
