from fastapi import FastAPI
from app.database import Base, engine
from app.routes import author_routes, book_routes, user_routes

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Digital Library API")

app.include_router(author_routes.router)
app.include_router(book_routes.router)
app.include_router(user_routes.router)

@app.get("/")
def root():
    return {"message": "Welcome to Digital Library!"}
