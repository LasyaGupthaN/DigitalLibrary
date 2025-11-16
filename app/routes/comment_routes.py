from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.dependencies import get_current_user
from app.models.comment import Comment

router = APIRouter(prefix="/comments", tags=["Comments"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/{book_id}")
def add_comment(book_id: int, data: dict, db: Session = Depends(get_db), user=Depends(get_current_user)):
    comment = Comment(book_id=book_id, user_id=user["user_id"], content=data["content"])
    db.add(comment)
    db.commit()
    return {"message": "Comment Added"}
