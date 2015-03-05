#!/usr/bin/env python3

from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData
from sqlalchemy.sql import select
from sqlalchemy.orm import sessionmaker
#from sqlalchemy.pool import NullPool
#import logging
#logging.basicConfig()
#logging.getLogger('sqlalchemy.engine').setLevel(logging.INFO)
#logging.getLogger('sqlalchemy.pool').setLevel(logging.INFO)


engine = create_engine('mysql+pymysql://root:111111@localhost/')#, echo=True, echo_pool=True) #, poolclass=NullPool)
res = engine.execute('create database if not exists foo;')
#res.close()


engine = create_engine('mysql+pymysql://root:111111@localhost/foo')#, echo=True, echo_pool=True) #, poolclass=NullPool)
Session = sessionmaker(bind=engine)

metadata = MetaData()

users = Table('users', metadata,
     Column('id', Integer, primary_key=True),
     Column('name', String(12)),
     Column('fullname', String(12)),
)

metadata.create_all(engine)

session = Session()
ins = users.insert().values(name='jack', fullname='Jack Jones')
session.execute(ins)
s = select([users])
res = session.execute(s)
for i in res:
    print(i)
session.commit()

#result.close()

# This is real reason of database lock

engine.execute('drop database foo;')
#engine.dispose()

#engine2 = create_engine('mysql+pymysql://root:111111@localhost/', echo=True, echo_pool=True)
