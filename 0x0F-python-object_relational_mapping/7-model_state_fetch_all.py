#!/usr/bin/python3
'''
script that lists all State objects from the database hbtn_0e_6_usa
'''

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    uri = 'mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        argv[1], argv[2], argv[3])
    engine = create_engine(uri)
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()
    for state in session.query(State).order_by(State.id).all():
        print(f"{state.id}: {state.name}")
