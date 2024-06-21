#!/usr/bin/python3
""" creates a connection to create a database and lists all states """

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
    c.execute("""SELECT * FROM states ORDER BY states.id ASC""")
    
    rows = c.fetchall()
    for row in rows:
        print(row)
