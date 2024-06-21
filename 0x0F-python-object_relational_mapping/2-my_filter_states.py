#!/usr/bin/python3
"""
takes an argument and displays all values in the states table
of hbtn_0e_0_usa where name matches the argument
"""

import MySQLdb
from sys import argv

if __name__ == '__main__':
    username = argv[1]
    password = argv[2]
    db = argv[3]
    s_name = argv[4]

    db = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=username,
        password=password,
        database=db
    )
    c = db.cursor()
    c.execute("SELECT * FROM states WHERE name = '{}' ORDER BY \
                states.id ASC".format(s_name))
    rows = c.fetchall()
    for row in rows:
        print(row)
    c.close()
    db.close()
