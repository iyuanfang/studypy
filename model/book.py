from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

from control.database import Base, engine

print("dbbook222222222222222")

# model里类名为DbBook
class DbBook(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(20))
    wordNum = Column(Integer)

    author_id = Column(Integer, ForeignKey("author.id"))

    author = relationship("DbAuthor", back_populates="books")

