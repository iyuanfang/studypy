from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# 连接sqlite数据库，相对路径
engine = create_engine("sqlite:///study.db")

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()

print("11111111111111111111")
Base.metadata.create_all(bind=engine)
print("end11111111111111111111")