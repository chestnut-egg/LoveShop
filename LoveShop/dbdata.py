from sqlalchemy import select,create_engine, Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from LoveShop.dbmysql import SQLALCHEMY_DATABASE_URI

Base = declarative_base()

class card(Base):
    # 表的名字:
    __tablename__ = 'card'
    # 表的结构:
    card_id = Column(Integer, primary_key=True,autoincrement=True)
    card_name = Column(String(20))
    card_type = Column(String(20))
    card_info = Column(String(20))
    card_price = Column(Integer)

class user(Base):
    __tablename__ = 'user'

    user_id = Column(Integer, primary_key=True,autoincrement=True)
    user_name = Column(String(20))
    user_account = Column(String(20))
    user_password = Column(String(20))

#创建表
# engine = create_engine(SQLALCHEMY_DATABASE_URI)
# Base.metadata.create_all(engine)
