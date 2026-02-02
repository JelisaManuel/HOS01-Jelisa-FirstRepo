#  Book Database Management System
#  This program allows users to add, remove, search, and display books and authors in a database.

from turtle import title


class BookDatabase:
    def __init__(self):
        self.books = {}
        self.authors = set()

# Add a new book to the database
    def add_book(self, title, author, year):
        if title not in self.books:
            self.books[title] = (author, year)
            self.authors.add(author)
            print(f"Book '{title}' added successfully.")
        else:
            print(f"Book '{title}' already exists in the database.")

# Remove a book from the database
    def remove_book(self, title):
        if title in self.books:
            author, _ = self.books.pop(title)
# Check if the author has other books
            if not any(book for book, (auth, _) in self.books.items() if auth == author):
                self.authors.remove(author)
            print(f"Book '{title}' removed successfully.")
        else:
            print(f"Book '{title}' not found in the database.")

# Search for a book by title

    def search_book(self, title):
        if title in self.books:
            author, year = self.books[title]
            print(f"Book found: '{title}' by {author}, published in {year}.")
        else:
            print(f"Book '{title}' not found.")

# Display all books in the database

    def display_books(self):
        if self.books:
            print("\nAll books in the database:")
            for title, (author, year) in self.books.items():
                print(f"'{title}' by {author}, published in {year}.")
        else:
            print("No books in the database.")

# Display all unique authors in the database

    def display_authors(self):
        if self.authors:
            print("\nUnique authors in the database:")
            for author in self.authors:
                print(author)
        else:
            print("No authors in the database.")

# Example usage
db = BookDatabase()
db.add_book("To Kill a Mockingbird", "Harper Lee", 1960)
db.add_book("1984", "George Orwell", 1949)
db.add_book("Brave New World", "Aldous Huxley", 1932)

# Display all books and authors
db.search_book("1984")
db.remove_book("A Book Not in Database")
db.display_authors()

# Remove a book and display updated lists
db.remove_book("1984")
db.display_books()
db.display_authors()