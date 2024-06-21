#!/usr/bin/python3
"""
takes in an argument and displays all values in the 
states table of hbtn_0e_0_usa where name matches the argument.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    username = argv[1]
    key = argv[2]
    database = argv[3]
    db = MySQLdb.connect(user=username, password=key, db=database)
    c = db.cursor()
    
    c.execute("SELECT * FROM states WHERE name = '{}'\
                ORDER BY states.id ASC".format(argv[4])
    )
    [print(row) for row in c.fetchall()]
