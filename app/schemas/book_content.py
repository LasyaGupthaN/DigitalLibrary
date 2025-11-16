from pydantic import BaseModel

class FullTextUpload(BaseModel):
    text: str
    page_size: int = 1000
