#!/usr/bin/python3
"""takes in the name of a state as
an argument and lists all cities of
that state, using the database hbtn_0e_4_usa"""

import sys
import MySQLdb

def list_cities_by_state(username, password, database, state_name):
    try:
        # Connect to the MySQL server
        db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

        # Create a cursor object using cursor() method
        cursor = db.cursor()

        # Prepare the SQL query with a parameter to list cities of the given state sorted by id in ascending order
        query = "SELECT * FROM cities WHERE state_name = %s ORDER BY id ASC"

        # Execute the SQL query with the state_name as a parameter
        cursor.execute(query, (state_name,))

        # Fetch all the rows
        rows = cursor.fetchall()

        # Display the results
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print("Error: {}".format(e))
    finally:
        # Close the database connection
        if db:
            db.close()

if __name__ == "__main__":
    # Get the arguments from the command line
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    state_name = sys.argv[4]

    # Call the function with the provided arguments
    list_cities_by_state(username, password, database, state_name)
