from pydantic import BaseModel
from app.enums import GenreEnum
from app.schemas.author import AuthorOut

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
