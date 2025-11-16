from pydantic import BaseModel
from app.enums import GenreEnum
from app.schemas.author import AuthorOut
from typing import Optional


class BookBase(BaseModel):
    title: str
    genre: GenreEnum
    author_id: int

class BookCreate(BookBase):
    pass

class BookOut(BookBase):
    id: int
    author: AuthorOut

    class Config:
        orm_mode = True


class BookUpdate(BaseModel):
    title: Optional[str] = None
    description: Optional[str] = None
    author_id: Optional[int] = None

    model_config = {"from_attributes": True}
