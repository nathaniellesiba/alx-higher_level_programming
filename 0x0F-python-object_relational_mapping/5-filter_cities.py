#!/usr/bin/python3
"""takes in the name of a state as
an argument and lists all cities of
that state, using the database hbtn_0e_4_usa"""

import sys
import MySQLdb

if __name__ == "__main__":
        username = sys.argv[1]
        password = sys.argv[2]
        database = sys.argv[3]
        state_name = sys.argv[4]

        db = MySQLdb.connect(host="localhost",
                user=username, passwd=password,
                db=database, port=3306)
        
        cursor = db.cursor()
        

        sql = """SELECT cities.name
          FROM states
          INNER JOIN cities ON states.id = cities.state_id
          WHERE states.name = %s
          ORDER BY cities.id ASC"""


        cursor.execute
        (sql, (state_name,))

        data = cursor.fetchall()
        
        for city in data:
            print(city)
        
        cursor.close()
        db.close()
