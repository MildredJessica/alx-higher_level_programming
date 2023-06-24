#!/usr/bin/python3
""" Connects to a database and selects the states"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2], database=sys.argv[3])
    cur = db.cursor()
    cur.execute("""SELECT * FROM states ORDER BY id ASC""")
    results = cur.fetchall()
    for row in results:
        print(row)

