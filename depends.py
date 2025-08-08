from typing import Generator
from sqlalchemy.orm import Session
from fastapi import Depends

from database.session import SessionLocal
from services.book import BookService

def get_db() -> Generator:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_book_service(db: Session = Depends(get_db)) -> BookService:
    return BookService(db)