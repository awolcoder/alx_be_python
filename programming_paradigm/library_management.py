# library_management.py

class Book:
    """Represents a book in the library."""

    def __init__(self, title, author):
        self.title = title            # Public attribute: book title
        self.author = author          # Public attribute: book author
        self._is_checked_out = False  # Private attribute to track availability

    def check_out(self):
        """Mark the book as checked out (unavailable)."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True  # Successfully checked out
        return False     # Book was already checked out

    def return_book(self):
        """Mark the book as returned (available)."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True  # Successfully returned
        return False     # Book was not checked out

    def is_available(self):
        """Check if the book is available."""
        return not self._is_checked_out


class Library:
    """Represents a collection of books in a library."""

    def __init__(self):
        self._books = []  # Private list to store Book instances

    def add_book(self, book):
        """Add a new book to the library collection."""
        self._books.append(book)

    def check_out_book(self, title):
        """
        Check out a book by title.
        Returns True if successful, False if the book is not found or already checked out.
        """
        for book in self._books:
            if book.title == title:
                return book.check_out()
        return False  # Book not found

    def return_book(self, title):
        """
        Return a book by title.
        Returns True if successful, False if the book is not found or was not checked out.
        """
        for book in self._books:
            if book.title == title:
                return book.return_book()
        return False  # Book not found

    def list_available_books(self):
        """Print the list of all available books in the library."""
        available_books = [book for book in self._books if book.is_available()]
        for book in available_books:
            print(f"{book.title} by {book.author}")
