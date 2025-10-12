class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        def __str__(self):
            return f"Book: '{self.title}' by {self.author}"

class EBook(Book):
    def __init__(self, title, author, file_size):
        super().__init__(title,author)
        self.file_size = file_size
        def __str__(self):
        return f"E-Book: '{self.title}' by {self.author} — File Size: {self.file_size}KB"


class PrintBook(Book):
    def __init__(self, title, author, page_count):
        super().__init__(title,author)
        self.page_count = page_count
         def __str__(self):
        return f"Print Book: '{self.title}' by {self.author} — Pages: {self.page_count}"

#Composition Class : Library
class Library:
    def __init__(self):
        self.books = [] # to store Book, EBook and PrintBook objects

    def add_book(self, book):
        if isinstance(book, Book):  # Ensure only valid book objects are added
            self.books.append(book)
        else:
            print("Error: Only Book, EBook, or PrintBook instances can be added.")

    def list_books(self):
        if not self.books:
            print("The library has no books.")
            return

        for book in self.books:
            if isinstance(book, EBook):
                print(f"E-Book: '{book.title}' by {book.author} — File Size: {book.file_size}MB")
            elif isinstance(book, PrintBook):
                print(f"Print Book: '{book.title}' by {book.author} — Pages: {book.page_count}")
            else:
                print(f"Book: '{book.title}' by {book.author}")

