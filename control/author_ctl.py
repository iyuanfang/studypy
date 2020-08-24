from typing import List

from model.author import DbAuthor
from view_model.author import Author
from .database import SessionLocal


class AuthorCtl:

    @classmethod
    def create_author(cls, author: Author):
        author = DbAuthor(**author.dict())
        session = SessionLocal()
        try:
            session.add(author)
            session.commit()
        finally:
            session.close()
        return {"code": 200}

    @classmethod
    def get_author(cls, id: int):
        session = SessionLocal()
        try:
            author = session.query(DbAuthor).filter(DbAuthor.id == id).first()
        finally:
            session.close()
        if author is None:
            return {}
        else:
            return Author(id=author.id, name=author.name)

    # 支持分页查询，page是页码，从0开始，page_size为每页记录数
    @classmethod
    def get_authors(cls, page: int, page_size: int):
        session = SessionLocal()
        l: List[Author] = []
        try:
            authors = session.query(DbAuthor).offset(page * page_size).limit(page_size).all()
        finally:
            session.close()
        for author in authors:
            l.append(Author(id=author.id, name=author.name))
        return l

    @classmethod
    def update_author(cls, author: Author):
        session = SessionLocal()
        try:
            author_for_update: DbAuthor = session.query(DbAuthor).filter(DbAuthor.id == author.id).first()
            if author_for_update is None:
                return {"code": 204}
            else:
                author_for_update.name = author.name
                session.commit()
                return {"code": 200}
        finally:
            session.close()

    @classmethod
    def delete_author(cls, id: int):
        session = SessionLocal()
        try:
            rows = session.query(DbAuthor).filter(DbAuthor.id == id).delete()
            session.commit()
        finally:
            session.close()
        return rows
