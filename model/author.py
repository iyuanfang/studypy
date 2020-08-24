from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from control.database import Base

print("dbauthor22222222222222222222")

# model里类名为DbBook
class DbAuthor(Base):
    __tablename__ = 'author'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(40))

    books = relationship("DbBook", back_populates="author")
