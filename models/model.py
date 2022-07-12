from sqlalchemy import Table, Column, INTEGER, VARCHAR
from connect.db import meta, engine

datas = Table('dataset', meta,
              Column('id', INTEGER(), primary_key=True, autoincrement=True),
              Column('data', VARCHAR(255)),
              )

meta.create_all(engine)
