#!/usr/bin/python3
"""prints the State object with
the name passed as argument from
the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

def print_state_id(username, password, database, state_name):
    try:
        # Create an engine to connect to the MySQL server
        engine = create_engine(f"mysql://{username}:{password}@localhost:3306/{database}")

        # Create a session
        Session = sessionmaker(bind=engine)
        session = Session()

        # Query to retrieve the State object based on the provided state name
        state = session.query(State).filter(State.name == state_name).first()

        # Display the result
        if state:
            print(state.id)
        else:
            print("Not found")

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
    state_name = sys.argv[4]

    # Call the function with the provided arguments
    print_state_id(username, password, database, state_name)
