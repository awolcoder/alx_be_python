# library_system.py

class Book:
    """
    Represents a generic book with a title and an author.

    Attributes:
        title (str): The title of the book.
        author (str): The author of the book.
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


class EBook(Book):
    """
    Represents an electronic book, inheriting from Book.

    Attributes:
        file_size (int): The size of the eBook file in KB.
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


class PrintBook(Book):
    """
    Represents a printed book, inheriting from Book.

    Attributes:
        page_count (int): The number of pages in the printed book.
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


class Library:
    """
    Represents a library containing a collection of books.

    Attributes:
        books (list): A list storing Book, EBook, and PrintBook instances.
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
        Lists all books in the library with their details.
        """
        for book in self.books:
            if isinstance(book, EBook):
                print(f"EBook: {book.title} by {book.author}, File Size: {book.file_size}KB")
            elif isinstance(book, PrintBook):
                print(f"PrintBook: {book.title} by {book.author}, Page Count: {book.page_count}")
            else:
                print(f"Book: {book.title} by {book.author}")
