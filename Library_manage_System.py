class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book_name):
        self.books.append({"name": book_name, "issued": False})
        print("Book added")

    def show_books(self):
        print("\n--- BOOK LIST ---")
        for i, book in enumerate(self.books, 1):
            status = "Issued" if book["issued"] else "Available"
            print(f"{i}. {book['name']} - {status}")

    def issue_book(self, book_name):
        for book in self.books:
            if book["name"].lower() == book_name.lower() and not book["issued"]:
                book["issued"] = True
                print("Book issued")
                return
        print("Book not available")

    def return_book(self, book_name):
        for book in self.books:
            if book["name"].lower() == book_name.lower() and book["issued"]:
                book["issued"] = False
                print("Book returned")
                return
        print("Invalid return request")


library = Library()

while True:
    print("\n=== LIBRARY MENU ===")
    print("1. Add Book")
    print("2. Show Books")
    print("3. Issue Book")
    print("4. Return Book")
    print("5. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        name = input("Enter book name: ")
        library.add_book(name)

    elif choice == "2":
        library.show_books()

    elif choice == "3":
        name = input("Enter book name to issue: ")
        library.issue_book(name)

    elif choice == "4":
        name = input("Enter book name to return: ")
        library.return_book(name)

    elif choice == "5":
        break

    else:
        print("Invalid choice")
