from sqlalchemy import Column, Integer, String

from control.database import Base


# model里类名为DbBook
class DbBook(Base):
    __tablename__ = 'Book'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(20))
    wordNum = Column(Integer)
