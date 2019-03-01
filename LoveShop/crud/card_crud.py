from sqlalchemy import select,create_engine, Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.orm import sessionmaker
from LoveShop.dbmysql import SQLALCHEMY_DATABASE_URI
from sqlalchemy.ext.declarative import declarative_base

from LoveShop.dbdata import card


engine = create_engine(SQLALCHEMY_DATABASE_URI)
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)


# 增加卡片
def add_card(card_name,card_type,card_info,card_price):
    #创建session对象:
    session = DBSession()
    # 创建新User对象:
    new_card = card(card_name=card_name, card_type=card_type, card_info=card_info, card_price=card_price)
    # 添加到session:
    session.add(new_card)
    # 提交即保存到数据库:
    session.commit()
    # 关闭session:
    session.close()


#返回卡片数量
def card_len():
    session = DBSession()
    ret1 = session.query(card).all()
    this_len = len(ret1)
    session.commit()
    session.close()
    return this_len


#返回卡片信息
def show_cardinfo(card_id):
    session = DBSession()
    ret = session.query(card).filter(card.card_id == card_id).all()

    dict={}
    dict['card_id'] = ret[0].card_id
    dict['card_name'] = ret[0].card_name
    dict['card_type'] = ret[0].card_type
    dict['card_info'] = ret[0].card_info
    dict['card_price'] = ret[0].card_price

    return dict



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

