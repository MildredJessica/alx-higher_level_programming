#!/usr/bin/python3
""""List all the cities based on the state name"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
            user=sys.argv[1], passwd=sys.argv[2],
            database=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT c.name, s.name FROM cities c \
            JOIN states s WHERE c.state_id = s.id \
            ORDER BY c.id")
    print(", ".join(
        [row[0] for row in cur.fetchall() if row[1] == sys.argv[4]]))
