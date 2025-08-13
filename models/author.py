# models/author.py
from sqlalchemy import Column, Integer, String, Date
from sqlalchemy.orm import relationship
from database.session import Base

class Author(Base):
    __tablename__ = "authors"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(100), index=True)
    last_name = Column(String(100), index=True)
    date_of_birth = Column(Date)
    biography = Column(String(1000), nullable=True)

    # Связь с книгами
    books = relationship("Book", back_populates="author")
