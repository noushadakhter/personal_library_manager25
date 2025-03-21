import json

# File Handling
def load_library():
    try:
        with open("library.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_library(library):
    with open("library.json", "w") as file:
        json.dump(library, file, indent=4)

def add_book(library):
    title = input("Enter book title: ")
    author = input("Enter author: ")
    year = int(input("Enter publication year: "))
    genre = input("Enter genre: ")
    read_status = input("Have you read this book? (yes/no): ").strip().lower() == "yes"
    new_book = {
        "title": title,
        "author": author,
        "publication_year": year,
        "genre": genre,
        "read_status": read_status
    }
    library.append(new_book)
    save_library(library)
    print("Book added successfully!\n")

def remove_book(library):
    title = input("Enter the title of the book to remove: ")
    library = [book for book in library if book["title"].lower() != title.lower()]
    save_library(library)
    print("Book removed successfully!\n")

def search_book(library):
    search_by = input("Search by (title/author): ").strip().lower()
    query = input("Enter search query: ").strip().lower()
    results = [book for book in library if query in book[search_by].lower()]
    if results:
        for book in results:
            print(f"{book['title']} by {book['author']} ({book['publication_year']}) - {book['genre']} - {'Read' if book['read_status'] else 'Unread'}")
    else:
        print("No matching books found!\n")

def display_books(library):
    if library:
        for book in library:
            print(f"{book['title']} by {book['author']} ({book['publication_year']}) - {book['genre']} - {'Read' if book['read_status'] else 'Unread'}")
    else:
        print("Library is empty!\n")

def display_statistics(library):
    total_books = len(library)
    read_books = sum(1 for book in library if book["read_status"])
    percent_read = (read_books / total_books * 100) if total_books > 0 else 0
    print(f"Total Books: {total_books}\nPercentage Read: {percent_read:.2f}%\n")

def main():
    library = load_library()
    while True:
        print("\nPersonal Library Manager")
        print("1. Add a book")
        print("2. Remove a book")
        print("3. Search for a book")
        print("4. Display all books")
        print("5. Display statistics")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            add_book(library)
        elif choice == "2":
            remove_book(library)
        elif choice == "3":
            search_book(library)
        elif choice == "4":
            display_books(library)
        elif choice == "5":
            display_statistics(library)
        elif choice == "6":
            save_library(library)
            print("Library saved to file. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again!\n")

if __name__ == "__main__":
    main()
