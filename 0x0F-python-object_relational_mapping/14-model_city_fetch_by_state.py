#!/usr/bin/python3
""" prints all City objects from the database hbtn_0e_14_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
            format(username, password, db_name),pool_pre_ping=True)
    
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    
    """creating a session"""
    session = Session()

    """extracting all cities in a state"""
    cities = session.query(State, City) \
            .order_by(City.id).all()

    """print all states"""
    for city in cities:
        print("{}: ({}) {}".format(city.state.name, city.id, city.name))


    session.close()
