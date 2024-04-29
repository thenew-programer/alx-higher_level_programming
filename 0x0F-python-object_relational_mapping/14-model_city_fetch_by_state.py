#!/usr/bin/python3
''' delete all State objs with a name containing a'''

import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    '''
    create engine, a session and
    delete the record from the db
    '''
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(City, State).join(State)
    for city, state in query.all():
        print(f"{state.name}:({city.id}) {city.name}")
    session.commit()
    session.close()
