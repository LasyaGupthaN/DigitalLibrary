from sqlalchemy.orm import Session
from app.models.author import Author
from app.schemas.author import AuthorCreate

def create_author(db: Session, data: AuthorCreate):
    author = Author(name=data.name)
    db.add(author)
    db.commit()
    db.refresh(author)
    return author

def get_authors(db: Session):
    return db.query(Author).all()
