# repositories/book.py
from sqlalchemy.orm import Session
from models.book import Book
from schemas.book import BookCreate

class BookRepository:
    """Слой работы с БД для книг"""

    def __init__(self, db: Session):
        self.db = db

    def get_books(self):
        return self.db.query(Book).all()

    def create_book(self, book_data: BookCreate):
        new_book = Book(**book_data.dict())
        self.db.add(new_book)
        self.db.commit()
        self.db.refresh(new_book)
        return new_book
