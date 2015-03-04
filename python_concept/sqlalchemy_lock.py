#!/usr/bin/env python3

import sqlalchemy

print('hello, alchemy')

from sqlalchemy import create_engine

engine = create_engine('mysql+pymysql://root:111111@localhost/foo', echo=True)

from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey

metadata = MetaData()

users = Table('users', metadata,
     Column('id', Integer, primary_key=True),
     Column('name', String(12)),
     Column('fullname', String(12)),
 )

metadata.create_all(engine) 

engine.execute('drop database foo;')
