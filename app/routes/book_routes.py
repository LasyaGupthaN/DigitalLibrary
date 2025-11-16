from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.schemas.book import BookCreate, BookOut, BookUpdate
from app.schemas.book_content import FullTextUpload
from app.services.book_service import create_book, get_books, update_book, delete_book
from app.dependencies import admin_required, get_current_user
from app.database import SessionLocal
from app.models.book_content import BookContent

router = APIRouter(prefix="/books", tags=["Books"])


# ---------- DB Dependency ----------
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# ---------- CREATE BOOK (ADMIN) ----------
@router.post("/", response_model=BookOut, dependencies=[Depends(admin_required)])
def add_book(book: BookCreate, db: Session = Depends(get_db)):
    return create_book(db, book)


# ---------- LIST ALL BOOKS ----------
@router.get("/", response_model=list[BookOut])
def list_books(db: Session = Depends(get_db)):
    return get_books(db)


# ---------- UPDATE BOOK (PATCH, ADMIN) ----------
@router.patch("/{book_id}", dependencies=[Depends(admin_required)])
def patch_book(book_id: int, data: BookUpdate, db: Session = Depends(get_db)):
    updated = update_book(db, book_id, data)

    if not updated:
        raise HTTPException(status_code=404, detail="Book not found")

    return {"message": "Book updated", "book": updated}


# ---------- DELETE BOOK (ADMIN) ----------
@router.delete("/{book_id}", dependencies=[Depends(admin_required)])
def delete_book_route(book_id: int, db: Session = Depends(get_db)):
    deleted = delete_book(db, book_id)

    if not deleted:
        raise HTTPException(status_code=404, detail="Book not found")

    return {"message": "Book deleted successfully"}


# ---------- UPLOAD FULL TEXT (ADMIN ONLY) ----------
@router.post("/{book_id}/upload_full_text", dependencies=[Depends(admin_required)])
def upload_full_text(book_id: int, data: FullTextUpload, db: Session = Depends(get_db)):
    # Remove existing pages for this book
    db.query(BookContent).filter(BookContent.book_id == book_id).delete()
    db.commit()

    page = 1
    for i in range(0, len(data.text), data.page_size):
        chunk = data.text[i:i + data.page_size]
        db.add(BookContent(book_id=book_id, page_number=page, content=chunk))
        page += 1

    db.commit()
    return {"message": "Content uploaded", "pages": page - 1}


# ---------- READ BOOK PAGE (USER MUST BE LOGGED IN) ----------
@router.get("/{book_id}/read")
def read_page(
    book_id: int,
    page: int,
    db: Session = Depends(get_db),
    user=Depends(get_current_user)     # ONLY authenticated users can read
):
    result = db.query(BookContent).filter_by(
        book_id=book_id,
        page_number=page
    ).first()

    if not result:
        raise HTTPException(status_code=404, detail="Page not found")

    return {
        "book_id": result.book_id,
        "page": result.page_number,
        "content": result.content
    }
