#!/usr/bin/python3
"""  lists all State objects from the database hbtn_0e_6_usa """

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    engine = create_engine("mysql+mysqldb://{}:{}@localhost/{}".format(
                                                                    argv[1],
                                                                    argv[2],
                                                                    argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    stmt = session.query(State).order_by(State.id)
    for row in stmt:
        print(f"{row.id}: {row.name}")
