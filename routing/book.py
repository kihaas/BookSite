# routing/book.py
from typing import List
from fastapi import APIRouter, Depends
from depends import get_book_service
from schemas.book import BookCreate, BookResponse
from services.book import BookService

router = APIRouter(prefix="/books", tags=["books"])

@router.get("", response_model=List[BookResponse])
async def get_all_books(book_service: BookService = Depends(get_book_service)):
    """Получение всех всех книг"""
    return book_service.get_books()

@router.post("", response_model=BookResponse)
async def create_book(
    book_data: BookCreate,
    book_service: BookService = Depends(get_book_service)
):
    """Создание книги"""
    return book_service.create_book(book_data)
