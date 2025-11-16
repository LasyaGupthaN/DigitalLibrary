from sqlalchemy.orm import Session
from app.models.book import Book
from app.schemas.book import BookCreate
from app.schemas.book import BookUpdate

def create_book(db: Session, data: BookCreate):
    book = Book(
        title=data.title,
        genre=data.genre,
        author_id=data.author_id
    )
    db.add(book)
    db.commit()
    db.refresh(book)
    return book

def get_books(db: Session):
    return db.query(Book).all()


def update_book(db: Session, book_id: int, data: BookUpdate):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        return None

    if data.title:
        book.title = data.title
    if data.description:
        book.description = data.description
    if data.author_id:
        book.author_id = data.author_id

    db.commit()
    db.refresh(book)
    return book


def delete_book(db: Session, book_id: int):
    book = db.query(Book).filter(Book.id == book_id).first()
    if not book:
        return False

    db.delete(book)
    db.commit()
    return True