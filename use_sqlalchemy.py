#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from model.book import DbBook
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

# 连接sqlite数据库
engine = create_engine("sqlite:///study.db")

# 生成Session
session = Session(engine)
print("sqlalchemy create session")

# 增加一条Book记录
book = DbBook(title="study py", wordNum=30000)
session.add(book)
session.commit()

# 查询Book表
books = session.query(DbBook).all()
for book in books:
    print("Book id=" + str(book.id) + ",title=" + book.title + ",wordNum=" + str(book.wordNum))

# 只取第一条记录
book = session.query(DbBook).first()
print("--Book id=" + str(book.id) + ",title=" + book.title + ",wordNum=" + str(book.wordNum))

# 加一个查询条件
book = session.query(DbBook).filter(DbBook.id == 2).first()
print("----Book id=" + str(book.id) + ",title=" + book.title + ",wordNum=" + str(book.wordNum))

# 修改
session.query(DbBook).filter(DbBook.id == 2).update({"title": "updated"})
session.commit()

# 删除
session.query(DbBook).filter(DbBook.id > 5).delete()
session.commit()

session.close()
