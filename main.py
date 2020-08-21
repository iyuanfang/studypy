from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from model.book import Book

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/books/{id}")
async def get_book(id):
    book=Book.get_book(id)
    return {"id": id,"title":book.title}

