#!/usr/bin/python3
""" lists all cities from the database hbtn_0e_4_usa """

import MySQLdb
from sys import argv

if __name__ == "__main__":

    db = MySQLdb.connect(user=argv[1], password=argv[2], db=argv[3])
    c = db.cursor()
    c.execute("""
        SELECT cities.id, cities.name, states.name FROM cities\
        INNER JOIN states ON states.id = cities.state_id ORDER \
        BY cities.id ASC """)
    [print(row) for row in c.fetchall()]
