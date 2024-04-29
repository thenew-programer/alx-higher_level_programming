#!/usr/bin/python3
'''
class definition of a City and an instance Base = declarative_base()
'''
from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base, State


class City(Base):
    '''
    State class inherits from SQLalchemy Base Class
    Attr:
        __tablename__(str): table name
        id (int): city table column
        name (str): city table column
        state_id (int): city table column
    '''
    __tablename__ = 'cities'
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
