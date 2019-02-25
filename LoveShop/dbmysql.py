from sqlalchemy import create_engine

engine = create_engine("mysql+pymysql://root:12345678@localhost:3306/dan", max_overflow=5)

cur = engine.execute('select * from card')
print(cur.fetchall())