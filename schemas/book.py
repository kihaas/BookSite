from datetime import date
from typing import Optional
from pydantic import BaseModel, Field, validator


class AuthorBase(BaseModel):
    first_name: str = Field(..., max_length=100, example="John")
    last_name: str = Field(..., max_length=100, example="Doe")
    date_of_birth: date = Field(..., example="1970-01-01")
    biography: Optional[str] = Field(None, max_length=1000, example="Famous author")


class AuthorCreate(AuthorBase):
    pass


class Author(AuthorBase):
    id: int

    class Config:
        orm_mode = True  # Для работы с ORM (например, SQLAlchemy)


class BookBase(BaseModel):
    title: str = Field(..., max_length=200, example="The Great Book")
    annotation: Optional[str] = Field(None, max_length=1000)
    date_published: date = Field(..., example="2020-01-01")
    author_id: int = Field(..., example=1)

    @validator('date_published')
    def date_published_must_be_past(cls, v):
        if v > date.today():
            raise ValueError('Date published cannot be in the future')
        return v


class BookCreate(BookBase):
    pass


class Book(BookBase):
    id: int
    author: Author  # Вложенная модель автора

    class Config:
        orm_mode = True