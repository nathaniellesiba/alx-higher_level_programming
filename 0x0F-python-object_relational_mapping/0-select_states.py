#!/usr/bin/python3
"""list of states in ascending order"""

import sys
import MySQLdb

if __name__ == "__main__":
        username = sys.argv[1]
            password = sys.argv[2]
                db_name = sys.argv[3]

                    db = MySQLdb.connect(host="localhost", user=username, passwd=password, db=db_name, port=3306)
                        cursor = db.cursor()
                            cursor.execute("SELECT * FROM states ORDER BY id")
                                data = cursor.fetchall()
                                    for row in data:
                                                print(row)
                                                    cursor.close()
                                                        db.close()
