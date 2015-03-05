#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy.sql import select #, sessionmaker
#from sqlalchemy.pool import NullPool
#Session = sessionmaker(bind=engine)
import logging

logging.basicConfig()
logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)
logging.getLogger('sqlalchemy.pool').setLevel(logging.INFO)


engine = create_engine('mysql+pymysql://root:111111@localhost/foo', echo=True, echo_pool=True) #, poolclass=NullPool)

metadata = MetaData()

users = Table('users', metadata,
     Column('id', Integer, primary_key=True),
     Column('name', String(12)),
     Column('fullname', String(12)),
)

#metadata.create_all(engine)

#ins = users.insert().values(name='jack', fullname='Jack Jones')
#result = conn.execute(ins)
#result.close()

conn = engine.connect()
s = select([users])
result = conn.execute(s)
#for row in result:
#    print(row)
#result.close()

# This is real reason of database lock
conn.close()

engine.execute('drop database foo;')
engine.dispose()

#engine2 = create_engine('mysql+pymysql://root:111111@localhost/', echo=True, echo_pool=True)
