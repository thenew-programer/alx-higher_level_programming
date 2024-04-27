#!/usr/bin/python3
"""
script that lists State objects
from the database hbtn_0e_6_usa
with id == 1
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    instance = session.query(State).filter(State.id == 1).first()
    if instance:
        print(instance.id, instance.name, sep=": ")
    else:
        print('Nothing')
    session.close()