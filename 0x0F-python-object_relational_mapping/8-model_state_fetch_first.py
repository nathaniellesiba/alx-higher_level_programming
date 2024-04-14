#!/usr/bin/python3
"""prints the first State object from the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from model_state import Base, State
from sqlalchemy.orm import sessionmaker

def print_first_state(username, password, database):
    try:
        # Create an engine to connect to the MySQL server
        engine = create_engine(f"mysql://{username}:{password}@localhost:3306/{database}")

        # Create a session
        Session = sessionmaker(bind=engine)
        session = Session()

        # Query to retrieve the first State object based on id
        first_state = session.query(State).order_by(State.id).first()

        # Display the result
        if first_state:
            print(f"{first_state.id}: {first_state.name}")
        else:
            print("Nothing")

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
    print_first_state(username, password, database)
