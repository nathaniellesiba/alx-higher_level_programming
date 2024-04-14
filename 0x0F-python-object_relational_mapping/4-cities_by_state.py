#!/usr/bin/python3
"""lists all cities from the
database hbtn_0e_4_usa"""
import sys
import MySQLdb

def list_cities(username, password, database):
        db = MySQLdb.connect(host="localhost", user=username, passwd=password, db=database, port=3306)
            cursor = db.cursor()
                cursor.execute("SELECT * FROM cities ORDER BY id")
                    data = cursor.fetchall()
                        for row in data:
                                    print(row)
                                        cursor.close()
                                            db.close()

                                            if __name__ == "__main__":
                                                    username = sys.argv[1]
                                                        password = sys.argv[2]
                                                            database = sys.argv[3]
                                                                list_cities(username, password, database)
