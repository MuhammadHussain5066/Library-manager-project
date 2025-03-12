import json
import os

# File where data is stored
FILE_PATH = 'library_data.json'

def load_library():
    """Loads the library from file if it exists, otherwise returns an empty list."""
    return json.load(open(FILE_PATH, 'r')) if os.path.exists(FILE_PATH) else []

def store_library(library_data):
    """Saves the updated library data back to the file."""
    with open(FILE_PATH, 'w') as file:
        json.dump(library_data, file, indent=4)

def add_new_book(library_data):
    """Takes user input and adds a new book to the library."""
    book_info = {
        "title": input("📖 Enter Book Title: "),
        "author": input("✍️ Enter Author Name: "),
        "year": input("📅 Enter Year of Publication: "),
        "genre": input("📚 Enter Genre: "),
        "read": input("✅ Have you read it? (yes/no): ").strip().lower() == 'yes'
    }

    library_data.append(book_info)
    store_library(library_data)
    print(f'✅ The book "{book_info["title"]}" has been successfully added!')

def delete_book(library_data):
    """Removes a book based on title input."""
    book_title = input("❌ Enter the title of the book to remove: ").strip()
    initial_count = len(library_data)
    
    library_data[:] = [book for book in library_data if book["title"].lower() != book_title.lower()]
    
    if len(library_data) < initial_count:
        store_library(library_data)
        print(f'✅ Book "{book_title}" was removed successfully.')
    else:
        print(f'⚠️ Book "{book_title}" was not found.')

def find_books(library_data):
    """Searches for books based on user input for title or author."""
    search_type = input("🔍 Search by (title/author): ").strip().lower()
    search_value = input(f"Enter the {search_type}: ").strip().lower()
    
    matches = [book for book in library_data if search_value in book.get(search_type, "").lower()]
    
    if matches:
        print("\n📚 Matching Books Found:")
        for book in matches:
            status = "✅ Read" if book['read'] else "❌ Not Read"
            print(f'- {book["title"]} by {book["author"]} ({book["year"]}) - {book["genre"]} - {status}')
    else:
        print("⚠️ No matching books found.")

def show_all_books(library_data):
    """Displays all books in the library."""
    if not library_data:
        print("📭 No books in your library.")
        return
    
    print("\n📚 Library Collection:")
    for index, book in enumerate(library_data, 1):
        status = "✅ Read" if book['read'] else "❌ Not Read"
        print(f'{index}. {book["title"]} by {book["author"]} ({book["year"]}) - {book["genre"]} - {status}')

def show_library_statistics(library_data):
    """Displays statistics about the library collection."""
    total = len(library_data)
    read_count = sum(1 for book in library_data if book['read'])
    read_percentage = (read_count / total * 100) if total else 0

    print("\n📊 Library Statistics:")
    print(f'📚 Total Books: {total}')
    print(f'📖 Books Read: {read_count} ({read_percentage:.1f}%)')

def main():
    """Main menu-driven program loop."""
    library_data = load_library()
    
    while True:
        print("\n📖 LIBRARY MENU")
        print("1️⃣ Add New Book")
        print("2️⃣ Remove a Book")
        print("3️⃣ Search for a Book")
        print("4️⃣ View All Books")
        print("5️⃣ View Library Statistics")
        print("6️⃣ Exit")

        option = input("➡️ Choose an option: ").strip()

        if option == '1':
            add_new_book(library_data)
        elif option == '2':
            delete_book(library_data)
        elif option == '3':
            find_books(library_data)
        elif option == '4':
            show_all_books(library_data)
        elif option == '5':
            show_library_statistics(library_data)
        elif option == '6':
            print("👋 Exiting Library Manager. Have a great day!")
            break
        else:
            print("⚠️ Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
