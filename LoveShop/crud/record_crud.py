from sqlalchemy import *
from sqlalchemy.orm import sessionmaker
from LoveShop.dbmysql import SQLALCHEMY_DATABASE_URI
from LoveShop.dbdata import record
import datetime


engine = create_engine(SQLALCHEMY_DATABASE_URI)
# 创建DBSession类型:
DBSession = sessionmaker(bind=engine)


# 增加用户
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
def find_record_by_user_id(user_id):
    session = DBSession()

    query = session.query(record).filter(
        record.user_id == user_id
    )

    isexist = session.query(
        query.exists()
    ).scalar()

    record = []

    record_id_list = []
    record_time_list = []
    record_type_list = []
    record_amount_list = []
    record_state_list = []

    if isexist == True:
        ret = session.query(record).filter(record.user_id == user_id).all()
        for i in range(len(ret)):
            record_id_list.append(ret[i].record_id)
            record_time_list.append(ret[i].record_time)
            record_type_list.append(ret[i].record_type)
            record_amount_list.append(ret[i].record_amount)
            record_state_list.append(ret[i].record_state)
    else:
        record_id_list.append(-1)

    record.append(record_id_list)
    record.append(record_time_list)
    record.append(record_type_list)
    record.append(record_amount_list)
    record.append(record_state_list)

    return record

# now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
# add_record(1,now_time,'购买卡片',5,'交易完成')

list = find_record_by_user_id(1)

print(list[0][0])