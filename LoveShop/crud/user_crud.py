from sqlalchemy import select,create_engine, Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.orm import sessionmaker
from LoveShop.dbmysql import SQLALCHEMY_DATABASE_URI
from sqlalchemy.ext.declarative import declarative_base

from LoveShop.dbdata import user


engine = create_engine(SQLALCHEMY_DATABASE_URI)
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)


# 增加用户
def add_user(user_name,user_account,user_password):
    #创建session对象:
    session = DBSession()
    # 创建新User对象:
    new_user = user(user_name=user_name, user_account=user_account, user_password=user_password)
    # 添加到session:
    session.add(new_user)
    # 提交即保存到数据库:
    session.commit()
    # 关闭session:
    session.close()

# 通过账号返回用户信息
def find_user_by_account(user_account):
    session = DBSession()

    query = session.query(user).filter(
        # user.user_account.in_(['Jack', 'Bob', 'Sandy']),
        user.user_account == user_account
    )

    isexist = session.query(
        query.exists()
    ).scalar()

    if isexist == True:
        ret = session.query(user).filter(user.user_account == user_account).all()
        dict = {}
        dict['user_id'] = ret[0].user_id
        dict['user_name'] = ret[0].user_name
        dict['user_account'] = ret[0].user_account
        dict['user_password'] = ret[0].user_password
    else:
        dict = {}
        dict['user_id'] = '-1'
        dict['user_name'] = '-1'
        dict['user_account'] = '-1'
        dict['user_password'] = '-1'

    return dict
