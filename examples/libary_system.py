"""
# Library Management System

## Learning Objectives
- Object-Oriented Programming (OOP)
- System Design
- Python Best Practices
- Real-world Application Modeling

## Key Concepts Demonstrated
- Class Design
- Composition
- Type Hinting
- Error Handling
- Complex System Interactions
"""

from datetime import datetime
from typing import List, Optional

# 1. MODELS: Core Data Structures
# --------------------------------

class Book:
    """
    Represents a book in the library system.
    
    Key Responsibilities:
    - Store book details
    - Track book availability
    """
    def __init__(self, title: str, author: str, isbn: str):
        """
        Initialize a book with its core attributes.
        
        Args:
            title (str): Book's title
            author (str): Book's author
            isbn (str): Unique book identifier
        """
        self.title = title
        self.author = author
        self.isbn = isbn
        self.is_available = True  # Track book availability status

    def __str__(self) -> str:
        """
        Provide a human-readable string representation of the book.
        
        Returns:
            str: Formatted book description
        """
        return f"{self.title} by {self.author} (ISBN: {self.isbn})"


class Member:
    """
    Represents a library member.
    
    Key Responsibilities:
    - Store member information
    - Unique identification
    """
    def __init__(self, name: str, member_id: int):
        """
        Initialize a library member.
        
        Args:
            name (str): Member's full name
            member_id (int): Unique member identifier
        """
        self.name = name
        self.member_id = member_id

    def __str__(self) -> str:
        """
        Provide a string representation of the member.
        
        Returns:
            str: Member details
        """
        return f"{self.name} (ID: {self.member_id})"


class BorrowingRecord:
    """
    Tracks the borrowing history of a book.
    
    Key Responsibilities:
    - Record book borrowing details
    - Generate unique record identifiers
    """
    def __init__(self, member: Member, book: Book, borrow_date: datetime):
        """
        Create a borrowing record.
        
        Args:
            member (Member): Member who borrowed the book
            book (Book): Borrowed book
            borrow_date (datetime): Date of borrowing
        """
        # Generate a unique record ID
        self.record_id = f"{member.member_id}-{book.isbn}-{borrow_date.strftime('%Y%m%d%H%M%S')}"
        self.member = member
        self.book = book
        self.borrow_date = borrow_date
        self.return_date = None

    def __str__(self) -> str:
        """
        Provide a detailed string representation of the borrowing record.
        
        Returns:
            str: Borrowing record details
        """
        return (
            f"Record ID: {self.record_id}, "
            f"Member: {self.member.name}, "
            f"Book: {self.book.title}, "
            f"Borrowed on: {self.borrow_date}"
        )


class Library:
    """
    Represents the library system.
    
    Key Responsibilities:
    - Manage book collection
    - Track library details
    """
    def __init__(self, name: str, location: str):
        """
        Initialize a library.
        
        Args:
            name (str): Library name
            location (str): Library location
        """
        self.name = name
        self.location = location
        self.books: List[Book] = []

    def add_book(self, book: Book) -> None:
        """Add a book to the library collection."""
        self.books.append(book)

    def remove_book(self, isbn: str) -> None:
        """
        Remove a book from the library by ISBN.
        
        Args:
            isbn (str): ISBN of the book to remove
        """
        self.books = [book for book in self.books if book.isbn != isbn]

    def list_books(self) -> List[Book]:
        """
        Retrieve all books in the library.
        
        Returns:
            List[Book]: List of all books
        """
        return self.books


class Librarian:
    """
    Represents a library staff member.
    
    Key Responsibilities:
    - Issue books
    - Manage library operations
    """
    def __init__(self, name: str, employee_id: int, library: Library):
        """
        Initialize a librarian.
        
        Args:
            name (str): Librarian's name
            employee_id (int): Unique employee identifier
            library (Library): Associated library
        """
        self.name = name
        self.employee_id = employee_id
        self.library = library

    def issue_book(self, member: Member, book: Book) -> Optional['BorrowingRecord']:
        """
        Issue a book to a member.
        
        Args:
            member (Member): Member borrowing the book
            book (Book): Book to be borrowed
        
        Returns:
            Optional[BorrowingRecord]: Borrowing record if successful, None otherwise
        """
        if book.is_available:
            book.is_available = False
            borrow_date = datetime.now()
            return BorrowingRecord(member, book, borrow_date)
        return None


# 2. CONTROLLER: Business Logic and Coordination
# ----------------------------------------------

class LibraryController:
    """
    Manages library operations and interactions.
    
    Key Responsibilities:
    - Coordinate between models
    - Implement CRUD operations
    """
    def __init__(self, library: Library, librarian: Librarian):
        """
        Initialize the library controller.
        
        Args:
            library (Library): Library being managed
            librarian (Librarian): Librarian managing the library
        """
        self.library = library
        self.librarian = librarian
        self.members: List[Member] = []
        self.borrowing_records: List[BorrowingRecord] = []

    # CREATE Operations
    def create_member(self, name: str, member_id: int) -> None:
        """Create a new library member."""
        member = Member(name, member_id)
        self.members.append(member)
        print(f"Member '{name}' with ID {member_id} created.")

    def create_book(self, title: str, author: str, isbn: str) -> None:
        """Add a new book to the library."""
        book = Book(title, author, isbn)
        self.library.add_book(book)
        print(f"Book '{title}' added to the library.")

    def create_borrowing_record(self, member: Member, book: Book) -> None:
        """Create a borrowing record for a book."""
        if book.is_available:
            record = self.librarian.issue_book(member, book)
            if record:
                self.borrowing_records.append(record)
                print(f"Borrowing record for '{book.title}' created successfully.")
        else:
            print(f"Book '{book.title}' is not available for borrowing.")

    # READ Operations
    def read_books(self) -> None:
        """Display all books in the library."""
        books = self.library.list_books()
        if books:
            print("Books available in the library:")
            for book in books:
                print(f"- {book}")
        else:
            print("No books available in the library.")

    def read_members(self) -> None:
        """Display all registered members."""
        if self.members:
            print("Registered members:")
            for member in self.members:
                print(f"- {member}")
        else:
            print("No registered members.")

    def read_borrowing_records(self) -> None:
        """Display all borrowing records."""
        if self.borrowing_records:
            print("Borrowing records:")
            for record in self.borrowing_records:
                print(f"{record}")
        else:
            print("No borrowing records found.")

    # UPDATE Operations
    def update_member_info(self, member_id: int, new_name: Optional[str] = None) -> None:
        """Update member information."""
        for member in self.members:
            if member.member_id == member_id:
                if new_name:
                    member.name = new_name
                    print(f"Member '{member_id}' updated with new name '{new_name}'.")
                return
        print(f"Member with ID {member_id} not found.")

    def update_book_info(self, isbn: str, new_title: Optional[str] = None, new_author: Optional[str] = None) -> None:
        """Update book information."""
        for book in self.library.books:
            if book.isbn == isbn:
                if new_title:
                    book.title = new_title
                if new_author:
                    book.author = new_author
                print(f"Book '{isbn}' updated. New title: '{book.title}', New author: '{book.author}'.")
                return
        print(f"Book with ISBN {isbn} not found.")

    # DELETE Operations
    def delete_member(self, member_id: int) -> None:
        """Remove a member from the system."""
        for member in self.members:
            if member.member_id == member_id:
                self.members.remove(member)
                print(f"Member '{member.name}' with ID {member_id} deleted.")
                return
        print(f"Member with ID {member_id} not found.")

    def delete_book(self, isbn: str) -> None:
        """Remove a book from the library."""
        for book in self.library.books:
            if book.isbn == isbn:
                self.library.remove_book(isbn)
                print(f"Book with ISBN {isbn} deleted.")
                return
        print(f"Book with ISBN {isbn} not found.")


# 3. USER INTERFACE
# -----------------

def print_menu() -> None:
    """Display the main menu options."""
    print("\n=== Library Management System ===")
    print("1. Register New Member")
    print("2. Add New Book")
    print("3. Borrow Book")
    print("4. View All Books")
    print("5. View All Members")
    print("6. View Borrowing Records")
    print("7. Update Member")
    print("8. Update Book")
    print("9. Delete Member")
    print("10. Delete Book")
    print("0. Exit")


def main() -> None:
    """
    Main program execution.
    Demonstrates the full workflow of the Library Management System.
    """
    # Initialize core components
    library = Library("City Library", "123 Main St")
    librarian = Librarian("Bob", 101, library)
    controller = LibraryController(library, librarian)

    # Main program loop
    while True:
        print_menu()
        choice = input("Select an option (0-10): ")

        try:
            if choice == "1":
                name = input("Enter member's name: ")
                member_id = int(input("Enter member ID: "))
                controller.create_member(name, member_id)

            elif choice == "2":
                title = input("Enter book title: ")
                author = input("Enter book author: ")
                isbn = input("Enter book ISBN: ")
                controller.create_book(title, author, isbn)

            elif choice == "3":
                controller.read_members()
                member_id = int(input("Enter member ID: "))
                controller.read_books()
                isbn = input("Enter book ISBN: ")
                
                # Find member and book
                member = next((m for m in controller.members if m.member_id == member_id), None)
                book = next((b for b in library.books if b.isbn == isbn), None)
                
                if member and book:
                    controller.create_borrowing_record(member, book)
                else:
                    print("Invalid member or book.")

            elif choice == "4":
                controller.read_books()

            elif choice == "5":
                controller.read_members()

            elif choice == "6":
                controller.read_borrowing_records()

            elif choice == "7":
                member_id = int(input("Enter member ID to update: "))
                new_name = input("Enter new name: ")
                controller.update_member_info(member_id, new_name)

            elif choice == "8":
                isbn = input("Enter book ISBN to update: ")
                new_title = input("Enter new title (optional): ")
                new_author = input("Enter new author (optional): ")
                controller.update_book_info(isbn, new_title, new_author)

            elif choice == "9":
                member_id = int(input("Enter member ID to delete: "))
                controller.delete_member(member_id)

            elif choice == "10":
                isbn = input("Enter book ISBN to delete: ")
                controller.delete_book(isbn)

            elif choice == "0":
                print("Exiting Library Management System. Goodbye!")
                break

            else:
                print("Invalid option. Please try again.")

        except ValueError:
            print("Invalid input. Please enter a valid value.")
        except Exception as e:
            print(f"An error occurred: {e}")


# Program Entry Point
if __name__ == "__main__":
    main()
