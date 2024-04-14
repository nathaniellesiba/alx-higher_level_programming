#!/usr/bin/python3
"""lists all State objects, and
corresponding City objects, contained
in the database hbtn_0e_101_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(username, password, db_name))
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id).all()

    for state in states:
        print("{}: {}".format(state.name, len(state.cities)))
        for city in state.cities:
            print("    {}: {}".format(city.id, city.name))
