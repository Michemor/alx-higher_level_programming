#!/usr/bin/python3
"""  lists all State objects from the database hbtn_0e_6_usa """

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine, select

engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                                                            argv[1],
                                                            argv[2],
                                                            argv[3]))
query = select(State).order_by(State.id)
with engine.connect() as conn:
    for row in conn.execute(query):
        print(f"{row.id} : {row.name}")
