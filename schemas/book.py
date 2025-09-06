# schemas/book.py
from datetime import date
from pydantic import BaseModel

# ====== Схемы для Авторoв ======

class AuthorBase(BaseModel):
    first_name: str
    last_name: str
    date_of_birth: date
    biography: str | None = None

class AuthorCreate(AuthorBase):
    """Схема для создания автора"""
    pass

class AuthorResponse(AuthorBase):
    """Схема для ответа (с ID)"""
    id: int

    class Config:
        from_attributes = True  # Pydantic v2: замена orm_mode


# ====== Схемы для Книг ======

class BookBase(BaseModel):
    title: str
    annotation: str | None = None
    date_published: date

class BookCreate(BookBase):
    """Схема для создания книги"""
    author_id: int  # ID автoра, к которому привязывается книга

class BookResponse(BookBase):
    """Схема для ответа (с ID и автором)"""
    id: int
    author: AuthorResponse

    class Config:
        from_attributes = True  # Pydantic v2: замена orm_mode
