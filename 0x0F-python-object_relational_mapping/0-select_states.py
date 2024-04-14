#!/usr/bin/python3
"""importing all lists from db"""
import MySQLdb
import sys

"""execution order"""
if__name__=='__main'__:
     db= MySQLdb.connect(host='localhost',port=3306, user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
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
