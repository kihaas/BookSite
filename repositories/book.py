from typing import List, Optional
from sqlalchemy.orm import Session
from models.book import Book as BookModel
from models.author import Author as AuthorModel
from schemas.book import Book, BookCreate, Author, AuthorCreate

class BookRepository:
    def __init__(self, db: Session):
        self.db = db

    def get_books(self, skip: int = 0, limit: int = 100) -> List[BookModel]:
        return self.db.query(BookModel).offset(skip).limit(limit).all()

    def get_book(self, book_id: int) -> Optional[BookModel]:
        return self.db.query(BookModel).filter(BookModel.id == book_id).first()

    def create_book(self, book: BookCreate) -> BookModel:
        db_book = BookModel(**book.dict())
        self.db.add(db_book)
        self.db.commit()
        self.db.refresh(db_book)
        return db_book

    def get_authors(self, skip: int = 0, limit: int = 100) -> List[AuthorModel]:
        return self.db.query(AuthorModel).offset(skip).limit(limit).all()

    def create_author(self, author: AuthorCreate) -> AuthorModel:
        db_author = AuthorModel(**author.dict())
        self.db.add(db_author)
        self.db.commit()
        self.db.refresh(db_author)
        return db_author