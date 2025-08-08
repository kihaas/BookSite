from typing import List, Optional
from sqlalchemy.orm import Session

from repositories.book import BookRepository
from schemas.book import Book, BookCreate, Author, AuthorCreate

class BookService:
    def __init__(self, db: Session):
        self.repository = BookRepository(db)

    def get_books(self, skip: int = 0, limit: int = 100) -> List[Book]:
        return self.repository.get_books(skip=skip, limit=limit)

    def get_book(self, book_id: int) -> Optional[Book]:
        return self.repository.get_book(book_id)

    def create_book(self, book: BookCreate) -> Book:
        return self.repository.create_book(book)

    def get_authors(self, skip: int = 0, limit: int = 100) -> List[Author]:
        return self.repository.get_authors(skip=skip, limit=limit)

    def create_author(self, author: AuthorCreate) -> Author:
        return self.repository.create_author(author)