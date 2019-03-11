from sqlalchemy import *
from sqlalchemy.orm import sessionmaker

from LoveShop.dbdata import *
from LoveShop.dbmysql import SQLALCHEMY_DATABASE_URI
import datetime


engine = create_engine(SQLALCHEMY_DATABASE_URI)
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)

#返回记录数量
def record_len(user_id):
    session = DBSession()

    ret = session.query(record).filter(record.user_id == user_id).all()

    this_len = len(ret)

    session.commit()
    session.close()
    return this_len


# 增加消费记录
def add_record(user_id,record_time,record_type,record_amount,record_state):
    #创建session对象:
    session = DBSession()
    # 创建新User对象:
    new_record = record(user_id=user_id, record_time=record_time, record_type=record_type,record_amount=record_amount,record_state=record_state)
    # 添加到session:
    session.add(new_record)
    # 提交即保存到数据库:
    session.commit()
    # 关闭session:
    session.close()

# 通过用户id返回消费记录
# 最外层为list 里面为rect
# 若为空 list[0]['record_id'] = -1
def find_record_by_user_id(user_id):

    session = DBSession()

    query = session.query(record).filter(
        record.user_id == user_id
    )

    isexist = session.query(
        query.exists()
    ).scalar()

    record_list = []

    if isexist == True:
        ret = session.query(record).filter(record.user_id == user_id).all()
        for i in range(len(ret)):
            this_record = {}
            this_record['record_id'] = ret[i].record_id
            this_record['record_time'] = ret[i].record_time
            this_record['record_type'] = ret[i].record_type
            this_record['record_amount'] = ret[i].record_amount
            this_record['record_state'] = ret[i].record_state
            record_list.append(this_record)
    else:
        this_record = {}
        this_record['record_id'] = -1
        record_list.append(this_record)

    return record_list

# now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
# add_record(1,now_time,'购买卡片',5,'交易完成')

# list = find_record_by_user_id(3)
# print(list[0]['record_id'])