#!/usr/bin/python3
""" lists all State objects from the database hbtn_0e_6_usa"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State  # Import the model_state module

def list_states(username, password, database):
        try:
            # Create an engine to connect to the MySQL server
            engine = create_engine(f"mysql://{username}:{password}@localhost:3306/{database}")

            # Bind the engine to the Base class
            Base.metadata.bind = engine

            # Create a session
            Session = sessionmaker(bind=engine)
            session = Session()

            # Query to retrieve all State objects and sort by id in ascending order
            states = session.query(State).order_by(State.id).all()

            # Display the results
            for state in states:
                print(f"{state.id}: {state.name}")

        except Exception as e:
            print(f"Error: {e}")
        finally:
            # Close the session
            if session is not None:
                session.close()

if __name__ == "__main__":
    # Ensure the required command-line arguments are provided
    if len(sys.argv) < 4:
        print("Usage: ./script.py <username> <password> <database>")
        sys.exit(1)

    # Get the arguments from the command line
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    # Call the function with the provided arguments
    list_states(username, password, database)
