#!/usr/bin/python3
""""List all the cities based on the state name"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
            user=sys.argv[1], passwd=sys.argv[2],
            database=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT * FROM cities c \
            INNER JOIN states s WHERE c.state_id = s.id and \
            s.name = %s ORDER BY c.id ASC", (sys.argv[4]))
    print(",".join(row[2]) for row in cur.fetchall())
