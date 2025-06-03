from lib.models import Borrower, Book
from config.setup import Session

session = Session()

# Clear existing data
print("Removing previous seed data...")
session.query(Borrower).delete()
session.query(Book).delete()
session.commit()

# Add borrowers
borrower1 = Borrower(
    first_name="Alice",
    last_name="Johnson",
    email="alice@example.com",
    phone="1234567890"
)

borrower2 = Borrower(
    first_name="Bob",
    last_name="Smith",
    email="bob@example.com",
    phone="2345678901"
)

# Add books
book1 = Book(
    title="Python Crash Course",
    author="Eric Matthes",
    isbn="9781593279288",
    genre="Programming"
)

book2 = Book(
    title="Clean Code",
    author="Robert Martin",
    isbn="9780132350884",
    genre="Software Development"
)

book3 = Book(
    title="The Pragmatic Programmer",
    author="Andrew Hunt",
    isbn="9780201616224",
    genre="Computer Science"
)

# Borrow some books
book1.available = False
book1.borrower = borrower1

book2.available = False
book2.borrower = borrower2

session.add_all([borrower1, borrower2, book1, book2, book3])
session.commit()

print("Seed data added successfully!")