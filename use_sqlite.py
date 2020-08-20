#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sqlite3

# 连接到SQLite库，文件是study.db
# 如果没有文件，会自动在当前目录创建
conn = sqlite3.connect('study.db')

print("sqlite opened")

# 创建一个cursor（游标）
c = conn.cursor()

# 执行创建表的SQL
c.execute('''CREATE TABLE Book
       (ID INTEGER PRIMARY KEY AUTOINCREMENT  NOT NULL,
       Title          TEXT    NOT NULL,
       WordNum          INT     NOT NULL);''')

conn.commit()
print("Table Book created successfully")


# 执行插入一条记录的SQL
# ID设置为自增，指定为null即可
c.execute("INSERT INTO Book (ID,Title,WordNum) values (null,'study py',100000)")
conn.commit()


# 执行一条查询SQL，获取多条记录
rows = c.execute("SELECT * from Book")
# 循环展示每条记录
for row in rows:
    print("Book id=" + str(row[0]) + ",title=" + row[1] + ",wordNum=" + str(row[2]))


# 执行一条update语句
c.execute("UPDATE Book set WordNum=200000 where ID=2")
# 需要commit数据
conn.commit()
# 查询ID=2的数据确认是否修改
row = c.execute("SELECT * from Book where ID=2").fetchone()
print("--Book id=" + str(row[0]) + ",title=" + row[1] + ",wordNum=" + str(row[2]))


# 执行一条delete语句，删除ID为1的那条
# 如果没有这条记录也不会报错
row=c.execute("DELETE from Book where ID=1")
# 打印删除了几条
print("delete rows:"+str(row.rowcount))
conn.commit()

conn.close()
