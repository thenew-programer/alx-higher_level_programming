#!/usr/bin/python3
'''
lass definition of a State and an instance Base = declarative_base()
'''
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    '''
    State class inherits from SQLalchemy Base Class
    Attr:
        __tablename__(str): table name
        id (int): state table column
        name (str): state table column
    '''
    __tablename__ = 'states'
    id = Column('id', Integer, nullable=False,
                primary_key=True, unique=True, autoincrement=True)
    name = Column('name', String(128), nullable=False)
