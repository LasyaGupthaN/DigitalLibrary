from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.book import BookCreate, BookOut
from app.services.book_service import create_book, get_books
from app.database import SessionLocal

router = APIRouter(prefix="/books", tags=["Books"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=BookOut)
def add_book(book: BookCreate, db: Session = Depends(get_db)):
    return create_book(db, book)

@router.get("/", response_model=list[BookOut])
def list_books(db: Session = Depends(get_db)):
    return get_books(db)
