#!/usr/bin/python3
"""script that takes in arg
and displays all values in the states
table of hbtn_0e_0_usa where name
matches the arg"""

import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]
    state_name = sys.argv[4]

    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=db_name)
    cur = db.cursor()
    cur.execute("SELECT * FROM states WHERE name = '{}' ORDER BY id ASC".format(state_name))

    for row in cur.fetchall():
        print(row)

    cur.close()
    db.close()
