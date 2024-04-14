#!/usr/bin/python3
""" adds the State object “Louisiana” to the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

def add_state(username, password, database):
    try:
        # Create an engine to connect to the MySQL server
        engine = create_engine(f"mysql://{username}:{password}@localhost:3306/{database}")

        # Bind the engine to the Base class
        Base.metadata.bind = engine

        # Create a session
        Session = sessionmaker(bind=engine)
        session = Session()

        # Create a new State object
        new_state = State(name="Louisiana")

        # Add the new State object to the session
        session.add(new_state)

        # Commit the session to persist the new State object to the database
        session.commit()

        # Print the new state's id
        print(new_state.id)

    except Exception as e:
        print(f"Error: {e}")
    finally:
        # Close the session
        if session is not None:
            session.close()

if __name__ == "__main__":
    # Get the arguments from the command line
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Call the function with the provided arguments
    add_state(username, password, database)
