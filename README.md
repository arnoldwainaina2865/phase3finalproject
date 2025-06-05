# 📚 Library Management System

A Python CLI application for managing library operations, built with SQLAlchemy ORM and Alembic for database migrations.



## Features

- **Book Management**:
  - Add/update/delete books
  - Search by title, author, or genre
  - Track availability status

- **Borrower Management**:
  - Register new borrowers
  - View borrowing history
  - Kenyan phone number validation (+254)

- **Loan System**:
  - Check-out/return books
  - Automatic availability updates
  - Relationship tracking (Borrower ↔ Books)

## 🛠️ Technologies Used

| Component       | Technology |
|-----------------|------------|
| Backend         | Python 3.8+ |
| ORM             | SQLAlchemy 2.0 |
| Database        | SQLite (with Alembic migrations) |
| CLI Framework   | Standard Python `input()`/`print()` |
| Dependency Mgmt | Pipenv |

## 🚀 Installation


# Clone repository


# Install dependencies
pipenv install

# Initialize database
pipenv run alembic upgrade head

# Seed sample data (optional)
pipenv run python seed.py