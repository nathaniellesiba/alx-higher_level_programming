#!/usr/bin/python3
"""lists all State objects that contain
the letter a from the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import func

def list_states_with_letter_a(username, password, database):
    try:
        # Create an engine to connect to the MySQL server
        engine = create_engine(f"mysql://{username}:{password}@localhost:3306/{database}")

        # Create a session
        Session = sessionmaker(bind=engine)
        session = Session()

        # Query to retrieve all State objects containing the letter 'a' and sort by id in ascending order
        states_with_a = session.query(State).filter(State.name.like('%a%')).order_by(State.id).all()

        # Display the results
        for state in states_with_a:
            print(f"{state.id}: {state.name}")

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
    list_states_with_letter_a(username, password, database)
