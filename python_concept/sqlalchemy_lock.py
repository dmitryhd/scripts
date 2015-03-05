#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy.sql import select

engine = create_engine('mysql+pymysql://root:111111@localhost/foo', echo=True, echo_pool=True)

metadata = MetaData()

users = Table('users', metadata,
     Column('id', Integer, primary_key=True),
     Column('name', String(12)),
     Column('fullname', String(12)),
 )

metadata.create_all(engine)

conn = engine.connect()

ins = users.insert().values(name='jack', fullname='Jack Jones')
result = conn.execute(ins)

s = select([users])
result = conn.execute(s)
for row in result:
    print(row)

engine.execute('drop database foo;')
