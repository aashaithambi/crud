class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

class Library:
    def __init__(self):
        self.books = []

    def create_book(self, title, author, year):
        book = Book(title, author, year)
        self.books.append(book)

    def read_all_books(self):
        for book in self.books:
            print(f"Title: {book.title}\nAuthor: {book.author}\nYear: {book.year}\n")

    def update_book(self, title, new_title, new_author, new_year):
        for book in self.books:
            if book.title == title:
                book.title = new_title
                book.author = new_author
                book.year = new_year
                print(f"Book {title} has been updated.")
                return
        print(f"Book {title} not found.")

    def delete_book(self, title):
        for book in self.books:
            if book.title == title:
                self.books.remove(book)
                print(f"Book {title} has been deleted.")
                return
        print(f"Book {title} not found.")


# Usage example
library = Library()

# Create books
library.create_book("Book 1", "Author 1", 2020)
library.create_book("Book 2", "Author 2", 2021)
library.create_book("Book 3", "Author 3", 2022)

# Read all books
library.read_all_books()

# Update a book
library.update_book("Book 2", "Updated Book 2", "Updated Author 2", 2023)

# Read all books after update
library.read_all_books()

# Delete a book
library.delete_book("Book 1")

# Read all books after delete
library.read_all_books()
