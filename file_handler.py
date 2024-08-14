import json

def save_books_to_file(books, filename='books.json'):
    with open(filename, 'w') as f:
        json.dump([book.__dict__ for book in books], f)

def load_books_from_file(filename='books.json'):
    try:
        with open(filename, 'r') as f:
            return [Book(**data) for data in json.load(f)]
    except FileNotFoundError:
        return []

def save_lent_books_to_file(lent_books, filename='lent_books.json'):
    with open(filename, 'w') as f:
        json.dump(lent_books, f)

def load_lent_books_from_file(filename='lent_books.json'):
    try:
        with open(filename, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []
