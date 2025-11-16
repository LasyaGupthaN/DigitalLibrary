from sqlalchemy import Column, Integer, String, Enum, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
from app.enums import GenreEnum

class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, nullable=False)
    genre = Column(Enum(GenreEnum), nullable=False)
    author_id = Column(Integer, ForeignKey("authors.id"))

  
    author = relationship("Author", back_populates="books")

    
    pages = relationship("BookContent", back_populates="book", cascade="all, delete")
    comments = relationship("Comment", back_populates="book", cascade="all, delete")
