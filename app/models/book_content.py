from sqlalchemy import Column, Integer, Text, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base

class BookContent(Base):
    __tablename__ = "book_contents"

    id = Column(Integer, primary_key=True)
    book_id = Column(Integer, ForeignKey("books.id"))
    page_number = Column(Integer, nullable=False)
    content = Column(Text, nullable=False)

    book = relationship("Book", back_populates="pages")
