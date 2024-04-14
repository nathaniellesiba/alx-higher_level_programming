#!/usr/bin/python3
"""importing all lists from db"""
import MySQLdb
import sys

def list_states(username, password, database):
    """connecting to the database"""
    db=_mysql.connect(host='localhost',port=3306, user=username, passwd=password, db=hbtn_0e_0_usa)
    c=db.cursor()

    """executing the SQL query"""
    c.execute("SELECT * FROM states ORDER BY id ASC")

    """fetching all rows"""
    rows = c.fetchall()

    """print results"""
    for row in rows:
        print(row)

    """close db connection"""
    db.close()

"""execution order"""
if__name__=='__main'__:
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    list_states(username, password, database)
