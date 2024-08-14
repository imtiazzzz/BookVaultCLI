def get_valid_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid floating number.")

def get_valid_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Please enter a valid integer.")

def display_menu():
    print("\nLibrary Management System")
    print("1. Add a book")
    print("2. View all books")
    print("3. Search books by title or ISBN")
    print("4. Search books by author")
    print("5. Remove a book")
    print("6. Lend a book")
    print("7. View lent books")
    print("8. Return a book")
    print("9. Exit")
