#!/usr/bin/python3
"""retrieve data from MySQL db"""

import sys
import MySQLdb

def get_state_data(username, password, dbname, state_name):
    try:
        # Connect to the MySQL server
        db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=dbname)

        # Create a cursor object using cursor() method
        cursor = db.cursor()

        # Prepare a SQL query with parameters to prevent SQL injection
        query = "SELECT * FROM states WHERE name = %s ORDER BY id ASC"

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
    if len(sys.argv) != 5:
        print("Usage: python script.py <username> <password> <dbname> <state_name>")
    else:
        username = sys.argv[1]
        password = sys.argv[2]
        dbname = sys.argv[3]
        state_name = sys.argv[4]
        get_state_data(username, password, dbname, state_name)
