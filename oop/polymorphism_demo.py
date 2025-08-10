import math

class Shape:
    """
    Base class representing a generic shape.
    """

    def area(self):
        """
        Calculates the area of the shape.
        Should be overridden by derived classes.

        Raises:
            NotImplementedError: If the method is not overridden in a subclass.
        """
        raise NotImplementedError("Subclasses must override the area() method.")


class Rectangle(Shape):
    """
    Class representing a rectangle, derived from Shape.

    Attributes:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.
    """

    def __init__(self, length, width):
        """
        Initializes a Rectangle instance.

        Args:
            length (float): The length of the rectangle.
            width (float): The width of the rectangle.
        """
        self.length = length
        self.width = width

    def area(self):
        """
        Calculates the area of the rectangle.

        Returns:
            float: The area of the rectangle.
        """
        return self.length * self.width


class Circle(Shape):
    """
    Class representing a circle, derived from Shape.

    Attributes:
        radius (float): The radius of the circle.
    """

    def __init__(self, radius):
        """
        Initializes a Circle instance.

        Args:
            radius (float): The radius of the circle.
        """
        self.radius = radius

    def area(self):
        """
        Calculates the area of the circle.

        Returns:
            float: The area of the circle.
        """
        return math.pi * (self.radius ** 2)
