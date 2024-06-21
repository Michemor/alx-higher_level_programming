#!/usr/bin/python3
"""
takes in arguments and displays all values in the
states table of hbtn_0e_0_usa where name matches the argument

Uses parametirized queries to prevent sql injection
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    state_name = argv[4]

    db = MySQLdb.connect(user=argv[1], password=argv[2], db=argv[3])
    c = db.cursor()
    query = """ SELECT * FROM states WHERE name = %s\
                ORDER BY states.id ASC"""
    c.execute(query, (argv[4],))
    [print(row) for row in c.fetchall()]
