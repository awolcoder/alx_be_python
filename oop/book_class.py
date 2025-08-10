# book_class.py

class Book:
    """
    A class representing a book with title, author, and publication year.
    
    Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
        year (int): The publication year of the book.
    """

    def __init__(self, title, author, year):
        """
        Constructor to initialize a Book instance.
        
        Args:
            title (str): The title of the book.
            author (str): The author of the book.
            year (int): The publication year of the book.
        """
        self.title = title
        self.author = author
        self.year = year

    def __del__(self):
        """
        Destructor that prints a message when the object is deleted.
        """
        print(f"Deleting {self.title}")

    def __str__(self):
        """
        Returns the informal string representation of the book.

        Returns:
            str: A human-readable description of the book.
        """
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """
        Returns the official string representation of the book
        that can be used to recreate the object.

        Returns:
            str: A string that represents the object in a way that could be used to recreate it.
        """
        return f"Book('{self.title}', '{self.author}', {self.year})"
