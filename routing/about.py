# routing/about.py
from typing import List
from fastapi import APIRouter, Depends
from depends import get_book_service
from schemas.book import BookCreate, BookResponse
from services.book import BookService


router = APIRouter(prefix="/about", tags=["about"])



