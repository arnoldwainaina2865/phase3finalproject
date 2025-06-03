#!/usr/bin/env python3

from config.setup import Session
from lib.models import Borrower, Book

session = Session()

class LibraryCLI:
    def __init__(self):
        self.session = Session()
        self.main_menu()

    def print_message(self, message):
        print(f"\n---\n{message}\n---\n")

    def validate_input(self, prompt, validation_func, error_msg):
        while True:
            user_input = input(prompt)
            if validation_func(user_input):
                return user_input
            print(error_msg)

    def main_menu(self):
        while True:
            print("\nLIBRARY MANAGEMENT SYSTEM")
            print("1. Borrower Operations")
            print("2. Book Operations")
            print("3. Borrow/Return Books")
            print("0. Exit")
            
            choice = input("Enter your choice: ")
            
            if choice == "0":
                self.print_message("Thank you for using the Library Management System!")
                break
            elif choice == "1":
                self.borrower_menu()
            elif choice == "2":
                self.book_menu()
            elif choice == "3":
                self.loan_menu()
            else:
                self.print_message("Invalid choice. Please try again.")

    def borrower_menu(self):
        while True:
            print("\nBORROWER OPERATIONS")
            print("1. Add Borrower")
            print("2. View All Borrowers")
            print("3. Find Borrower by ID")
            print("4. Update Borrower")
            print("5. Delete Borrower")
            print("6. View Borrower's Books")
            print("0. Back to Main Menu")
            
            choice = input("Enter your choice: ")
            
            if choice == "0":
                break
            elif choice == "1":
                self.add_borrower()
            elif choice == "2":
                self.view_all_borrowers()
            elif choice == "3":
                self.find_borrower_by_id()
            elif choice == "4":
                self.update_borrower()
            elif choice == "5":
                self.delete_borrower()
            elif choice == "6":
                self.view_borrower_books()
            else:
                self.print_message("Invalid choice. Please try again.")

    def book_menu(self):
        while True:
            print("\nBOOK OPERATIONS")
            print("1. Add Book")
            print("2. View All Books")
            print("3. Find Book by ID")
            print("4. Find Book by Title")
            print("5. Update Book")
            print("6. Delete Book")
            print("0. Back to Main Menu")
            
            choice = input("Enter your choice: ")
            
            if choice == "0":
                break
            elif choice == "1":
                self.add_book()
            elif choice == "2":
                self.view_all_books()
            elif choice == "3":
                self.find_book_by_id()
            elif choice == "4":
                self.find_book_by_title()
            elif choice == "5":
                self.update_book()
            elif choice == "6":
                self.delete_book()
            else:
                self.print_message("Invalid choice. Please try again.")

    def loan_menu(self):
        while True:
            print("\nBOOK LOAN OPERATIONS")
            print("1. Borrow Book")
            print("2. Return Book")
            print("0. Back to Main Menu")
            
            choice = input("Enter your choice: ")
            
            if choice == "0":
                break
            elif choice == "1":
                self.borrow_book()
            elif choice == "2":
                self.return_book()
            else:
                self.print_message("Invalid choice. Please try again.")

    # Borrower CRUD operations
    def add_borrower(self):
        try:
            first_name = self.validate_input(
                "Enter first name: ",
                lambda x: len(x) > 0,
                "First name cannot be empty."
            )
            last_name = self.validate_input(
                "Enter last name: ",
                lambda x: len(x) > 0,
                "Last name cannot be empty."
            )
            email = self.validate_input(
                "Enter email: ",
                lambda x: "@" in x,
                "Invalid email format."
            )
            phone = self.validate_input(
                "Enter phone number: ",
                lambda x: x.isdigit() and len(x) >= 10,
                "Phone must be at least 10 digits."
            )
            
            borrower = Borrower(
                first_name=first_name,
                last_name=last_name,
                email=email,
                phone=phone
            )
            
            self.session.add(borrower)
            self.session.commit()
            self.print_message("Borrower added successfully!")
            
        except Exception as e:
            self.session.rollback()
            self.print_message(f"Error: {str(e)}")

    def view_all_borrowers(self):
        borrowers = self.session.query(Borrower).all()
        if not borrowers:
            self.print_message("No borrowers found.")
            return
            
        for borrower in borrowers:
            print(f"\nID: {borrower.id}")
            print(f"Name: {borrower.first_name} {borrower.last_name}")
            print(f"Email: {borrower.email}")
            print(f"Phone: {borrower.phone}")
            print(f"Joined: {borrower.created_at}")

    def find_borrower_by_id(self):
        borrower_id = self.validate_input(
            "Enter borrower ID: ",
            lambda x: x.isdigit(),
            "ID must be a number."
        )
        
        borrower = self.session.query(Borrower).get(borrower_id)
        if borrower:
            print(f"\nID: {borrower.id}")
            print(f"Name: {borrower.first_name} {borrower.last_name}")
            print(f"Email: {borrower.email}")
            print(f"Phone: {borrower.phone}")
        else:
            self.print_message("Borrower not found.")

    def update_borrower(self):
        borrower_id = self.validate_input(
            "Enter borrower ID to update: ",
            lambda x: x.isdigit(),
            "ID must be a number."
        )
        
        borrower = self.session.query(Borrower).get(borrower_id)
        if not borrower:
            self.print_message("Borrower not found.")
            return
            
        print("\nLeave blank to keep current value.")
        first_name = input(f"First name ({borrower.first_name}): ") or borrower.first_name
        last_name = input(f"Last name ({borrower.last_name}): ") or borrower.last_name
        email = input(f"Email ({borrower.email}): ") or borrower.email
        phone = input(f"Phone ({borrower.phone}): ") or borrower.phone
        
        try:
            borrower.first_name = first_name
            borrower.last_name = last_name
            borrower.email = email
            borrower.phone = phone
            self.session.commit()
            self.print_message("Borrower updated successfully!")
        except Exception as e:
            self.session.rollback()
            self.print_message(f"Error: {str(e)}")

    def delete_borrower(self):
        borrower_id = self.validate_input(
            "Enter borrower ID to delete: ",
            lambda x: x.isdigit(),
            "ID must be a number."
        )
        
        borrower = self.session.query(Borrower).get(borrower_id)
        if borrower:
            try:
                self.session.delete(borrower)
                self.session.commit()
                self.print_message("Borrower deleted successfully!")
            except Exception as e:
                self.session.rollback()
                self.print_message(f"Error: {str(e)}")
        else:
            self.print_message("Borrower not found.")

    def view_borrower_books(self):
        borrower_id = self.validate_input(
            "Enter borrower ID: ",
            lambda x: x.isdigit(),
            "ID must be a number."
        )
        
        borrower = self.session.query(Borrower).get(borrower_id)
        if not borrower:
            self.print_message("Borrower not found.")
            return
            
        if not borrower.borrowed_books:
            self.print_message("This borrower has no books checked out.")
            return
            
        print(f"\nBooks borrowed by {borrower.first_name} {borrower.last_name}:")
        for book in borrower.borrowed_books:
            print(f"\nTitle: {book.title}")
            print(f"Author: {book.author}")
            print(f"ISBN: {book.isbn}")
            print(f"Genre: {book.genre}")

    # Book CRUD operations
    def add_book(self):
        try:
            title = self.validate_input(
                "Enter book title: ",
                lambda x: len(x) > 0,
                "Title cannot be empty."
            )
            author = self.validate_input(
                "Enter author: ",
                lambda x: len(x) > 0,
                "Author cannot be empty."
            )
            isbn = self.validate_input(
                "Enter ISBN: ",
                lambda x: len(x) >= 10,
                "ISBN must be at least 10 characters."
            )
            genre = input("Enter genre (optional): ") or None
            published_year = input("Enter published year (optional): ") or None
            
            book = Book(
                title=title,
                author=author,
                isbn=isbn,
                genre=genre,
                published_year=published_year
            )
            
            self.session.add(book)
            self.session.commit()
            self.print_message("Book added successfully!")
            
        except Exception as e:
            self.session.rollback()
            self.print_message(f"Error: {str(e)}")

    def view_all_books(self):
        books = self.session.query(Book).all()
        if not books:
            self.print_message("No books found.")
            return
            
        for book in books:
            status = "Available" if book.available else f"Borrowed by: {book.borrower.first_name} {book.borrower.last_name}"
            print(f"\nID: {book.id}")
            print(f"Title: {book.title}")
            print(f"Author: {book.author}")
            print(f"ISBN: {book.isbn}")
            print(f"Status: {status}")

    def find_book_by_id(self):
        book_id = self.validate_input(
            "Enter book ID: ",
            lambda x: x.isdigit(),
            "ID must be a number."
        )
        
        book = self.session.query(Book).get(book_id)
        if book:
            status = "Available" if book.available else f"Borrowed by: {book.borrower.first_name} {book.borrower.last_name}"
            print(f"\nID: {book.id}")
            print(f"Title: {book.title}")
            print(f"Author: {book.author}")
            print(f"ISBN: {book.isbn}")
            print(f"Genre: {book.genre}")
            print(f"Published Year: {book.published_year}")
            print(f"Status: {status}")
        else:
            self.print_message("Book not found.")

    def find_book_by_title(self):
        title = input("Enter book title (or part of it): ")
        books = self.session.query(Book).filter(Book.title.ilike(f"%{title}%")).all()
        
        if not books:
            self.print_message("No books found.")
            return
            
        for book in books:
            status = "Available" if book.available else f"Borrowed by: {book.borrower.first_name} {book.borrower.last_name}"
            print(f"\nID: {book.id}")
            print(f"Title: {book.title}")
            print(f"Author: {book.author}")
            print(f"Status: {status}")

    def update_book(self):
        book_id = self.validate_input(
            "Enter book ID to update: ",
            lambda x: x.isdigit(),
            "ID must be a number."
        )
        
        book = self.session.query(Book).get(book_id)
        if not book:
            self.print_message("Book not found.")
            return
            
        print("\nLeave blank to keep current value.")
        title = input(f"Title ({book.title}): ") or book.title
        author = input(f"Author ({book.author}): ") or book.author
        isbn = input(f"ISBN ({book.isbn}): ") or book.isbn
        genre = input(f"Genre ({book.genre}): ") or book.genre
        published_year = input(f"Published Year ({book.published_year}): ") or book.published_year
        
        try:
            book.title = title
            book.author = author
            book.isbn = isbn
            book.genre = genre
            book.published_year = published_year
            self.session.commit()
            self.print_message("Book updated successfully!")
        except Exception as e:
            self.session.rollback()
            self.print_message(f"Error: {str(e)}")

    def delete_book(self):
        book_id = self.validate_input(
            "Enter book ID to delete: ",
            lambda x: x.isdigit(),
            "ID must be a number."
        )
        
        book = self.session.query(Book).get(book_id)
        if book:
            try:
                self.session.delete(book)
                self.session.commit()
                self.print_message("Book deleted successfully!")
            except Exception as e:
                self.session.rollback()
                self.print_message(f"Error: {str(e)}")
        else:
            self.print_message("Book not found.")

    # Loan operations
    def borrow_book(self):
        borrower_id = self.validate_input(
            "Enter borrower ID: ",
            lambda x: x.isdigit(),
            "ID must be a number."
        )
        book_id = self.validate_input(
            "Enter book ID: ",
            lambda x: x.isdigit(),
            "ID must be a number."
        )
        
        borrower = self.session.query(Borrower).get(borrower_id)
        book = self.session.query(Book).get(book_id)
        
        if not borrower:
            self.print_message("Borrower not found.")
            return
        if not book:
            self.print_message("Book not found.")
            return
        if not book.available:
            self.print_message("Book is already borrowed.")
            return
            
        try:
            book.available = False
            book.borrower = borrower
            self.session.commit()
            self.print_message(f"Book '{book.title}' borrowed by {borrower.first_name} {borrower.last_name}")
        except Exception as e:
            self.session.rollback()
            self.print_message(f"Error: {str(e)}")

    def return_book(self):
        book_id = self.validate_input(
            "Enter book ID to return: ",
            lambda x: x.isdigit(),
            "ID must be a number."
        )
        
        book = self.session.query(Book).get(book_id)
        if not book:
            self.print_message("Book not found.")
            return
        if book.available:
            self.print_message("Book is not currently borrowed.")
            return
            
        borrower = book.borrower
        try:
            book.available = True
            book.borrower = None
            self.session.commit()
            self.print_message(f"Book '{book.title}' returned by {borrower.first_name} {borrower.last_name}")
        except Exception as e:
            self.session.rollback()
            self.print_message(f"Error: {str(e)}")

if __name__ == "__main__":
    LibraryCLI()