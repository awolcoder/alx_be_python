class Book:
    """
    Represents a generic book with a title and an author.
    """

    def __init__(self, title, author):
        """
        Initializes a Book instance.

        Args:
            title (str): The title of the book.
            author (str): The author of the book.
        """
        self.title = title
        self.author = author

    def __str__(self):
        """
        Returns the string representation of a Book.
        """
        return f"Book: {self.title} by {self.author}"


class EBook(Book):
    """
    Represents an electronic book, inheriting from Book.
    """

    def __init__(self, title, author, file_size):
        """
        Initializes an EBook instance.

        Args:
            title (str): The title of the eBook.
            author (str): The author of the eBook.
            file_size (int): The size of the eBook file in KB.
        """
        super().__init__(title, author)
        self.file_size = file_size

    def __str__(self):
        """
        Returns the string representation of an EBook.
        """
        return f"EBook: {self.title} by {self.author}, File Size: {self.file_size}KB"


class PrintBook(Book):
    """
    Represents a printed book, inheriting from Book.
    """

    def __init__(self, title, author, page_count):
        """
        Initializes a PrintBook instance.

        Args:
            title (str): The title of the printed book.
            author (str): The author of the printed book.
            page_count (int): The number of pages in the printed book.
        """
        super().__init__(title, author)
        self.page_count = page_count

    def __str__(self):
        """
        Returns the string representation of a PrintBook.
        """
        return f"PrintBook: {self.title} by {self.author}, Page Count: {self.page_count}"


class Library:
    """
    Represents a library containing a collection of books.
    """

    def __init__(self):
        """
        Initializes a Library instance with an empty list of books.
        """
        self.books = []

    def add_book(self, book):
        """
        Adds a book to the library collection.

        Args:
            book (Book): An instance of Book, EBook, or PrintBook.
        """
        self.books.append(book)

    def list_books(self):
        """
        Lists all books in the library by printing their string representations.
        """
        for book in self.books:
            print(book)
