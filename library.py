from book import Book
from file_handler import save_books_to_file, load_books_from_file, save_lent_books_to_file, load_lent_books_from_file

class Library:
    def __init__(self):
        self.books = load_books_from_file()
        self.lent_books = load_lent_books_from_file()

    def add_book(self, title, authors, isbn, year, price, quantity):
        new_book = Book(title, authors, isbn, year, price, quantity)
        self.books.append(new_book)
        save_books_to_file(self.books)
        print("Book added successfully!")

    def view_books(self):
        if not self.books:
            print("No books available.")
            return
        for book in self.books:
            print(book)

    def search_books(self, query):
        results = [book for book in self.books if query.lower() in book.title.lower() or query.lower() in book.isbn.lower()]
        if results:
            for book in results:
                print(book)
        else:
            print("No books found.")

    def search_books_by_author(self, author_name):
        results = [book for book in self.books if author_name.lower() in ', '.join(book.authors).lower()]
        if results:
            for book in results:
                print(book)
        else:
            print("No books found.")

    def remove_book(self, query):
        for book in self.books:
            if query.lower() in book.title.lower() or query.lower() in book.isbn.lower():
                self.books.remove(book)
                save_books_to_file(self.books)
                print("Book removed successfully!")
                return
        print("Book not found.")

    def lend_book(self, query, lender_name):
        for book in self.books:
            if query.lower() in book.title.lower() or query.lower() in book.isbn.lower():
                if book.quantity > 0:
                    book.quantity -= 1
                    self.lent_books.append({'title': book.title, 'isbn': book.isbn, 'lent_to': lender_name})
                    save_books_to_file(self.books)
                    save_lent_books_to_file(self.lent_books)
                    print(f"Book lent to {lender_name}.")
                    return
                else:
                    print("Not enough books available to lend.")
                    return
        print("Book not found.")

    def return_book(self, query):
        for record in self.lent_books:
            if query.lower() in record['title'].lower() or query.lower() in record['isbn'].lower():
                for book in self.books:
                    if book.title == record['title'] and book.isbn == record['isbn']:
                        book.quantity += 1
                        self.lent_books.remove(record)
                        save_books_to_file(self.books)
                        save_lent_books_to_file(self.lent_books)
                        print("Book returned successfully!")
                        return
        print("No matching lent book record found.")

    def view_lent_books(self):
        if not self.lent_books:
            print("No books are currently lent.")
            return
        for record in self.lent_books:
            print(f"Title: {record['title']}, ISBN: {record['isbn']}, Lent to: {record['lent_to']}")
