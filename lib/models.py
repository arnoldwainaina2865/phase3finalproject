from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

Base = declarative_base()

class Borrower(Base):
    __tablename__ = "borrowers"
    
    id = Column(Integer, primary_key=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String(100), nullable=False, unique=True)
    phone = Column(String, nullable=False, unique=True)
    created_at = Column(DateTime(), default=datetime.now())
    
    borrowed_books = relationship("Book", back_populates="borrower")

    def __repr__(self):
        return f"{self.first_name} {self.last_name}"

class Book(Base):
    __tablename__ = "books"
    
    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    author = Column(String, nullable=False)
    isbn = Column(String, nullable=False, unique=True)
    genre = Column(String, nullable=True)
    published_year = Column(Integer, nullable=True)
    available = Column(Integer, nullable=False, default=1)
    created_at = Column(DateTime(), default=datetime.now())
    
    borrower_id = Column(Integer, ForeignKey("borrowers.id"))
    borrower = relationship("Borrower", back_populates="borrowed_books")