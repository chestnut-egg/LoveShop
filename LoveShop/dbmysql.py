from sqlalchemy import create_engine


SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:12345678@localhost:3306/dan"
SQLALCHEMY_COMMIT_ON_TEARDOWN = True
SQLALCHEMY_TRACK_MODIFICATIONS = True


# engine = create_engine(SQLALCHEMY_DATABASE_URI, max_overflow=5)
# cur = engine.execute('select * from card')
# print(cur.fetchall())

