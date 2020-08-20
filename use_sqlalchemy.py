#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from model.book import Book
from sqlalchemy import create_engine
from sqlalchemy.orm import Session


engine = create_engine("sqlite:///study.db")

session = Session(engine)
print("sqlalchemy create session")

books = session.query(Book).all()
for book in books:
    print("Book id=" + str(book.id) + ",title=" + book.title + ",wordNum=" + str(book.wordNum))

session.close()
