from typing import List

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from view_model.book import Book
from control.book_ctl import BookCtl

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/books/{id}")
async def get_book(id):
    book: Book = BookCtl.get_book(id)
    return book


# 查询book，支持分页查询
# page和page_size为查询参数，而且有默认值，调用时可以不传，也可以通过?page=1&page_size=3这样来传入
@app.get("/books/")
def get_books(page: int = 0, page_size: int = 20):
    books = BookCtl.get_books(page, page_size)
    return books


@app.delete("/books/{id}")
async def delete_book(id):
    rows: int = BookCtl.delete_book(id)
    # 被删除的row数，应该=1
    if rows == 1:
        return {"code": 200}
    else:
        return {"code": 204}


@app.put("/books/")
async def create_book(book: Book):
    return BookCtl.create_book(book)


@app.patch("/books/")
async def update_book(book: Book):
    return BookCtl.update_book(book)
