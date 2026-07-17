from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

# 创建数据库引擎
engine = create_engine("sqlite:///chat.db")

# 基础类，所有表都继承他
Base = declarative_base()

# 定义一个Message表
class Message(Base):
    __tablename__ = "messages"  # 表名

    id = Column()
