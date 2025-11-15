from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.author import AuthorCreate, AuthorOut
from app.services.author_service import create_author, get_authors
from app.database import SessionLocal

router = APIRouter(prefix="/authors", tags=["Authors"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/", response_model=AuthorOut)
def add_author(author: AuthorCreate, db: Session = Depends(get_db)):
    return create_author(db, author)

@router.get("/", response_model=list[AuthorOut])
def list_authors(db: Session = Depends(get_db)):
    return get_authors(db)
