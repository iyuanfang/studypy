from typing import List

from .database import SessionLocal
from model.book import DbBook
from view_model.book import Book as Book


class BookCtl:

    @classmethod
    def create_book(cls, book: Book):
        book = DbBook(**book.dict())
        session = SessionLocal()
        try:
            session.add(book)
            session.commit()
        finally:
            session.close()
        return {"code": 200}

    @classmethod
    def update_book(cls, book: Book):
        # book = DbBook(**book.dict())
        session = SessionLocal()
        try:
            book_for_update: DbBook = session.query(DbBook).filter(DbBook.id == book.id).first()
            if book_for_update is None:
                return {"code": 204}
            else:
                book_for_update.title = book.title
                book_for_update.wordNum = book.wordNum
                session.commit()
                return {"code": 200}
        finally:
            session.close()

    @classmethod
    def get_book(cls, id: int):
        session = SessionLocal()
        try:
            book = session.query(DbBook).filter(DbBook.id == id).first()
        finally:
            session.close()
        if book is None:
            return {}
        else:
            return Book(id=book.id, title=book.title, wordNum=book.wordNum)

    # 支持分页查询，page是页码，从0开始，page_size为每页记录数
    @classmethod
    def get_books(cls, page: int, page_size: int):
        session = SessionLocal()
        l: List[Book] = []
        try:
            books = session.query(DbBook).offset(page * page_size).limit(page_size).all()
        finally:
            session.close()
        for book in books:
            l.append(Book(id=book.id, title=book.title, wordNum=book.wordNum))
        return l

    @classmethod
    def delete_book(cls, id: int):
        session = SessionLocal()
        try:
            rows = session.query(DbBook).filter(DbBook.id == id).delete()
            session.commit()
        finally:
            session.close()
        return rows
