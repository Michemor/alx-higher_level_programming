#!/usr/bin/python3
"""lists all states with a name starting with N """

import MySQLdb
from sys import argv

if __name__ == '__main__':
    username = argv[1]
    password = argv[2]
    db = argv[3]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        password=password,
        database=db
    )
    c = db.cursor()
    c.execute(
        """
        SELECT * FROM states WHERE UPPER(LEFT(name, 1)) = 'N'
        ORDER BY states.id ASC"""
    )
    rows = c.fetchall()
    for row in rows:
        print(row)
