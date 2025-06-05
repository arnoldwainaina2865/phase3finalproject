from lib.models import Borrower, Book
from config.setup import Session
from datetime import datetime

session = Session()

print("Removing previous seed data...")
session.query(Borrower).delete()
session.query(Book).delete()
session.commit()

borrowers = [
    Borrower(
        first_name="Wanjiru",
        last_name="Kamau",
        email="wanjiru.kamau@example.com",
        phone="254712345678"
    ),
    Borrower(
        first_name="Kipchoge",
        last_name="Omondi",
        email="kipchoge.omondi@example.com",
        phone="254723456789"
    ),
    Borrower(
        first_name="Auma",
        last_name="Atieno",
        email="auma.atieno@example.com",
        phone="254734567890"
    ),
    Borrower(
        first_name="Mwangi",
        last_name="Gitonga",
        email="mwangi.gitonga@example.com",
        phone="254745678901"
    ),
    Borrower(
        first_name="Nyambura",
        last_name="Wairimu",
        email="nyambura.w@example.com",
        phone="254756789012"
    )
]

books = [
    Book(
        title="Things Fall Apart",
        author="Chinua Achebe",
        isbn="9780385474542",
        genre="African Literature",
        published_year=1958,
        available=False,
        borrower=borrowers[0]  
    ),
    Book(
        title="Weep Not, Child",
        author="Ngũgĩ wa Thiong'o",
        isbn="9780143106692",
        genre="African Literature",
        published_year=1964,
        available=True
    ),
    Book(
        title="Half of a Yellow Sun",
        author="Chimamanda Ngozi Adichie",
        isbn="9780007200283",
        genre="Historical Fiction",
        published_year=2006,
        available=False,
        borrower=borrowers[1]  
    ),
    Book(
        title="The River Between",
        author="Ngũgĩ wa Thiong'o",
        isbn="9780435905484",
        genre="African Literature",
        published_year=1965,
        available=True
    ),
    Book(
        title="Americanah",
        author="Chimamanda Ngozi Adichie",
        isbn="9780007356348",
        genre="Contemporary Fiction",
        published_year=2013,
        available=True
    ),
    Book(
        title="Petals of Blood",
        author="Ngũgĩ wa Thiong'o",
        isbn="9780143105428",
        genre="Political Fiction",
        published_year=1977,
        available=False,
        borrower=borrowers[2]  
    ),
    Book(
        title="The Secret Lives of Baba Segi's Wives",
        author="Lola Shoneyin",
        isbn="9781846685193",
        genre="Family Drama",
        published_year=2010,
        available=True
    ),
    Book(
        title="So Long a Letter",
        author="Mariama Bâ",
        isbn="9780435911980",
        genre="Epistolary Novel",
        published_year=1979,
        available=True
    ),
    Book(
        title="Nervous Conditions",
        author="Tsitsi Dangarembga",
        isbn="9780954702335",
        genre="Coming-of-Age",
        published_year=1988,
        available=True
    ),
    Book(
        title="The Fishermen",
        author="Chigozie Obioma",
        isbn="9780316338370",
        genre="Tragedy",
        published_year=2015,
        available=False,
        borrower=borrowers[3]  
    )
]

session.add_all(borrowers)
session.add_all(books)
session.commit()

print(f"Successfully seeded:\n- {len(borrowers)} Kenyan borrowers\n- {len(books)} famous African books")
print(f"Current checkouts: {sum(1 for book in books if not book.available)} books borrowed")