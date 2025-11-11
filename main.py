from library_books import library_books
from datetime import datetime, timedelta
import itertools

def display_menu():
    print("\n**Menu**")
    print("1.View available books")
    print("2.Search")
    print("3.Checkout")
    print("4.Return")
    print("5.View overdue books")
    print("6.View top 3 most checked out books!")
    print("7.Exit")
display_menu()
user_response = input(f'Enter a number between 1-7')

# -------- Level 1 --------
# TODO: Create a function to view all books that are currently available
# Output should include book ID, title, and author
if user_response == "1":
    print(library_books)

# -------- Level 2 --------
# TODO: Create a function to search books by author OR genre
# Search should be case-insensitive
# Return a list of matching books

books_db = [
    {"id": "B1", "title": "The Lightning Thief", "author": "Rick Riordan", "genres": ["Fantasy", "Young Adult"], "similar": ["B6"]},
    {"id": "B2", "title": "To Kill a Mocking Bird", "author": "Harper Lee", "genres": ["Historical", "Classic"], "similar": []},
    {"id": "B3", "title": "The Great Gatsby", "author": "F. Scott Fitzgerald", "genres": ["Classic"], "similar": []},
    {"id": "B4", "title": "1984", "author": "George Orwell", "genres": ["Dystopian", "Classic"], "similar": []},
    {"id": "B5", "title": "Pride and Prejudice", "author": "Jane Austen", "genres": ["Classic", "Romance"], "similar": []},
    {"id": "B6", "title": "The Hobbit", "author": "J.R.R. Tolkien", "genres": ["Fantasy", "Classic"], "similar": ["B1"]},
    {"id": "B7", "title": "Fahrenheit 451", "author": "Ray Bradbury", "genres": ["Dystopian", "Classic"], "similar": []},
    {"id": "B8", "title": "The Catcher in the Rye", "author": "J.D. Salinger", "genres": ["Classic"], "similar": []},
]
def search_books():

    if user_response == "2":
        print(f'Search bar activated')
    search_query = input(f'Enter author or genre to search: ')
    results = search_books(search_query, books_db)

    if results:
        print(f"\nFound {len(results)} matching book(s):")
        for book in results:
            print(f"Title: {book['title']}, Author: {book['author']}, ID: {book['id']}")
    else:
        print(f"No books found matching '{search_query}'.")

    # The original code's follow-up question
    user_response = input(f'\nLooking for anything else? ')


# -------- Level 3 --------
# TODO: Create a function to checkout a book by ID
# If the book is available:
#   - Set the due_date to 2 weeks from today
#   - Increment the checkouts counter
# If it is not available:
#   - Mark it unavailable
#   - Print a message saying it's already checked out





# -------- Level 4 --------
# TODO: Create a function to return a book by ID
# Set its availability to True and clear the due_date

# TODO: Create a function to list all overdue books
# A book is overdue if its due_date is before today AND it is still checked out


# -------- Level 5 --------
# TODO: Convert your data into a Book class with methods like checkout() and return_book()
# TODO: Add a simple menu that allows the user to choose different options like view, search, checkout, return, etc.

# -------- Optional Advanced Features --------
# You can implement these to move into Tier 4:
# - Add a new book (via input) to the catalog
# - Sort and display the top 3 most checked-out books
# - Partial title/author search
# - Save/load catalog to file (CSV or JSON)
# - Anything else you want to build on top of the system!

if __name__ == "__main__":
    # You can use this space to test your functions
    pass
