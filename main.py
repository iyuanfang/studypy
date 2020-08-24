from typing import List

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles

from control.author_ctl import AuthorCtl
from control.database import Base, engine
from view_model.author import Author
from view_model.book import Book
from control.book_ctl import BookCtl

print("start22222222222222222211")
Base.metadata.create_all(bind=engine)
print("end22222222222222222211")

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/book/{id}")
async def get_book(id):
    book: Book = BookCtl.get_book(id)
    return book


# 查询book，支持分页查询
# page和page_size为查询参数，而且有默认值，调用时可以不传，也可以通过?page=1&page_size=3这样来传入
@app.get("/book/")
def get_books(page: int = 0, page_size: int = 20):
    books = BookCtl.get_books(page, page_size)
    return books


@app.delete("/book/{id}")
async def delete_book(id):
    rows: int = BookCtl.delete_book(id)
    # 被删除的row数，应该=1
    if rows == 1:
        return {"code": 200}
    else:
        return {"code": 204}


@app.put("/book/")
async def create_book(book: Book):
    return BookCtl.create_book(book)


@app.patch("/book/")
async def update_book(book: Book):
    return BookCtl.update_book(book)


@app.get("/author/{id}")
async def get_author(id):
    author: Author = AuthorCtl.get_author(id)
    return author


@app.get("/author/")
def get_authors(page: int = 0, page_size: int = 20):
    authors = AuthorCtl.get_authors(page, page_size)
    return authors


@app.put("/author/")
def create_author(author: Author):
    return AuthorCtl.create_author(author)

@app.patch("/author/")
async def update_author(author: Author):
    return AuthorCtl.update_author(author)

@app.delete("/author/{id}")
async def delete_author(id):
    rows: int = AuthorCtl.delete_author(id)
    # 被删除的row数，应该=1
    if rows == 1:
        return {"code": 200}
    else:
        return {"code": 204}
