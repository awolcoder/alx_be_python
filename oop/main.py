from book_class import Book

def main():
    my_book = Book("1984", "George Orwell", 1949)

    # __str__ demonstration
    print(my_book)  # "1984 by George Orwell, published in 1949"

    # __repr__ demonstration
    print(repr(my_book))  # "Book('1984', 'George Orwell', 1949)"

    # Trigger __del__
    del my_book

if __name__ == "__main__":
    main()
