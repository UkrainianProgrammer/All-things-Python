class Library:
    def __init__(self, name):
        self.name = name
        self.books = []
    
    def add_book(self, book):
        if not isinstance(book, Book):
            raise ValueError("Book must be an instance of Book class.")
        else:
            self.books.append(book)

class Book:
    def __init__(self, title, author, isbn):
        self.title = title
        self.author = author
        self.isbn = isbn
    
    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, ISBN: {self.isbn}"
