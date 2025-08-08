from typing import List
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from depends import get_db, get_book_service
from schemas.book import Book, BookCreate, Author, AuthorCreate
from services.book import BookService

router = APIRouter(prefix="/books", tags=["books"])

@router.get(
    "",
    response_model=List[Book],
    summary="Get all books",
    description="Retrieve a list of all books with pagination",
    responses={
        404: {"description": "No books found"},
        500: {"description": "Internal server error"}
    }
)
async def get_all_books(
    skip: int = 0,
    limit: int = 100,
    book_service: BookService = Depends(get_book_service)
) -> List[Book]:
    try:
        books = book_service.get_books(skip=skip, limit=limit)
        if not books:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="No books found"
            )
        return books
    except Exception as e:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=str(e)
        )

@router.post(
    "",
    response_model=Book,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new book",
    description="Create a new book with the given data",
    responses={
        400: {"description": "Invalid input data"},
        422: {"description": "Validation error"}
    }
)
async def create_book(
    book: BookCreate,
    book_service: BookService = Depends(get_book_service)
) -> Book:
    return book_service.create_book(book)

@router.get(
    "/authors",
    response_model=List[Author],
    summary="Get all authors",
    description="Retrieve a list of all authors"
)
async def get_all_authors(
    skip: int = 0,
    limit: int = 100,
    book_service: BookService = Depends(get_book_service)
) -> List[Author]:
    return book_service.get_authors(skip=skip, limit=limit)

@router.post(
    "/authors",
    response_model=Author,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new author",
    description="Create a new author with the given data"
)
async def create_author(
    author: AuthorCreate,
    book_service: BookService = Depends(get_book_service)
) -> Author:
    return book_service.create_author(author)