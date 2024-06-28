#!/usr/bin/python3

"""
takes the name of a state as an argument
Lists all cities of that state

comprises of a join between states and cities table
where the state_id = cities_id
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    state_name = argv[4];

    db = MySQLdb.connect(user=argv[1], password=argv[2], database=argv[3])
    cur = db.cursor()
    cur.execute("""
                SELECT * FROM cities INNER JOIN states ON \
                states.id = cities.state_id ORDER BY cities.id ASC""")
    print(", ".join([row[2] for row in cur.fetchall() if row[4] == argv[4]]))
