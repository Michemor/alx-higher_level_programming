#!/usr/bin/python3
"""
lists all State objects that contain the letter a
from the database hbtn_0e_6_usa
"""

from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import select, create_engine
import sys

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    r = session.query(State).filter(State.name.like('%a%')).order_by(State.id)
    for row in r:
        print(f"{row.id}: {row.name}")
