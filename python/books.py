FILENAME = "books.txt"

def add_book():
    book_name = input("Enter book title: ")
    # Open file in append mode ('a') to add the new book
    with open(FILENAME, "a") as file:
        file.write(book_name + "\n")
    print(f"'{book_name}' added successfully!\n")

def view_books():
    print("\n--- All Books ---")
    try:
        with open(FILENAME, "r") as file:
            books = file.readlines()
            if not books:
                print("No books found.")
            else:
                for i, book in enumerate(books, 1):
                    print(f"{i}. {book.strip()}")
    except FileNotFoundError:
        print("No book file found yet. Add a book first!")
    print("-" * 17)

def main():
    while True:
        print("\n1. Add Book")
        print("2. View Books")
        print("3. Exit")
        
        choice = input("Choose an option (1-3): ")
        
        if choice == '1':
            add_book()
        elif choice == '2':
            view_books()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
