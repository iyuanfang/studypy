from sqlalchemy import create_engine
from sqlalchemy.orm import Session

# 连接sqlite数据库，相对路径
engine = create_engine("sqlite:///study.db")
print("sqlite connected")

class DB:
    @classmethod
    def get_session(cls):
        return Session(engine)
