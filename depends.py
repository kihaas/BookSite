# depends.py
from database.session import get_db
from repositories.book import BookRepository
from services.book import BookService
from fastapi import Depends
from sqlalchemy.orm import Session

def get_book_service(db: Session = Depends(get_db)) -> BookService:
    """DI для сервиса книг"""
    repository = BookRepository(db)
    return BookService(repository)
