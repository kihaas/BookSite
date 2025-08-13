# services/book.py
from typing import List
from repositories.book import BookRepository
from schemas.book import BookCreate, BookResponse

class BookService:
    """Бизнес-логика для книг"""

    def __init__(self, repository: BookRepository) -> None:
        self.repository = repository

    def get_books(self) -> List[BookResponse]:
        return self.repository.get_books()

    def create_book(self, book_data: BookCreate) -> BookResponse:
        return self.repository.create_book(book_data)
