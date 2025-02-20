class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
    
    def add_book(self, book):
        if not isinstance(book, Book):
            raise ValueError("Book must be an instance of Book class.")
        else:
            self.books.append(book)
    
    def remove_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                break
        else:
            print(f"Book '{title}' not found in the library.")

    def display_books(self):
        if self.books:
            for book in self.books:
                print(book)
        else:
            print("No books are stored in the library.")
    
    def search_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        else:
            print(f"Book '{title}' not found in the library.")


class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
    
    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}"
