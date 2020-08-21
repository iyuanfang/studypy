from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from model.db import DB

Base = declarative_base()


class Book(Base):
    __tablename__ = 'Book'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(20))
    wordNum = Column(Integer)

    @classmethod
    def create_book(cls, book):
        session = DB.get_session()
        session.add(book)
        session.commit()
        session.close()


    @classmethod
    def get_book(cls, id: int):
        session = DB.get_session()
        book=session.query(Book).filter(Book.id == id).first()
        session.close()
        return book
