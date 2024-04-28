#!/usr/bin/python3
'''
update db record where name
is New Mexico
and id = 2
'''

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    '''
    create engine, a session and
    update the record to the db
    '''
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()
    session.update(State) .filter(State.id == 2)
    session.close()
