#!/usr/bin/python3
"""lists all cities from the database hbtn_0e_4_usa"""

import sys
import MySQLdb

def list_cities(username, password, database):
    try:
        # Connect to the MySQL server
        db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

        # Create a cursor object using cursor() method
        cursor = db.cursor()

        # Prepare the SQL query to list all cities sorted by id in ascending order
        query = "SELECT * FROM cities ORDER BY id ASC"

        # Execute the SQL query
        cursor.execute(query)

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

    # Call the function with the provided arguments
    list_cities(username, password, database)
