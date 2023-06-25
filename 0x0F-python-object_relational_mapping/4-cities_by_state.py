#!/usr/bin/python3
""""List all the cities"""
import sys
import MySQLdb

if __name__ == "__main__":
    db = MySQLdb.connect(
            user=sys.argv[1], passwd=sys.argv[2],
            database=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT c.id, c.name, s.name \
            FROM cities c JOIN states s WHERE c.state_id = s.id \
            ORDER BY c.id ASC")
    [print(row) for row in cur.fetchall()]
