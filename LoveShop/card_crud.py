from sqlalchemy import select,create_engine, Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from LoveShop.dbdata import card


SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:12345678@localhost:3306/dan"
engine = create_engine(SQLALCHEMY_DATABASE_URI)
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

def add(card_name,card_type,card_info,card_price):
    #创建session对象:
    session = DBSession()
    # 创建新User对象:
    new_user = card(card_name=card_name, card_type=card_type, card_info=card_info, card_price=card_price)
    # 添加到session:
    session.add(new_user)
    # 提交即保存到数据库:
    session.commit()
    # 关闭session:
    session.close()


#返回卡片数量
def card_line():
    session = DBSession()

    ret1 = session.query(card).all()

    line = len(ret1)
    print(line)

    session.commit()
    session.close()
    return line



def read():
    session = DBSession()

    ret1 = session.query(card).all()
    ret2 = session.query(card.card_id, card.card_name).all()
    ret3 = session.query(card).filter(card.card_id == '1').all()
    ret4 = session.query(card.card_name).filter(card.card_id == '1').all()

    # print(len(ret1))
    # print(ret1[1].card_name)
    # print(ret2)
    # print(ret3[0].card_name)
    # print(ret4)

    session.commit()
    session.close()



read()