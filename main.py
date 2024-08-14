from library import Library
from utils import display_menu, get_valid_float, get_valid_int

def main():
    library = Library()

    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            title = input("Enter book title: ")
            authors = input("Enter authors (comma-separated): ").split(',')
            isbn = input("Enter ISBN: ")
            year = get_valid_int("Enter publishing year: ")
            price = get_valid_float("Enter price: ")
            quantity = get_valid_int("Enter quantity: ")
            library.add_book(title, authors, isbn, year, price, quantity)
        
        elif choice == '2':
            library.view_books()

        elif choice == '3':
            query = input("Enter title or ISBN to search: ")
            library.search_books(query)

        elif choice == '4':
            author_name = input("Enter author name to search: ")
            library.search_books_by_author(author_name)

        elif choice == '5':
            query = input("Enter title or ISBN to remove: ")
            library.remove_book(query)

        elif choice == '6':
            query = input("Enter title or ISBN to lend: ")
            lender_name = input("Enter the name of the lender: ")
            library.lend_book(query, lender_name)

        elif choice == '7':
            library.view_lent_books()

        elif choice == '8':
            query = input("Enter title or ISBN to return: ")
            library.return_book(query)

        elif choice == '9':
            print("Exiting the system. Goodbye!")
            break

        else:
            print("Invalid choice! Please select a valid option.")

if __name__ == "__main__":
    main()
