#!/usr/bin/python3
""" Connects to a database and selects
the details of a state based on the name"""

import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
            user=sys.argv[1], passwd=sys.argv[2],
            database=sys.argv[3])
    cur = db.cursor()
    cur.execute("""SELECT * FROM states""")
    [print(state) for state in cur.fetchall() if state[1] == sys.argv[4]]
