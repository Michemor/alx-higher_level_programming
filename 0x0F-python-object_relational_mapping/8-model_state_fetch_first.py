#!/usr/bin/python3
""" prints the first State object from the database hbtn_0e_6_usa """

from model_state import Base, State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine, select
from sys import argv


if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
            argv[1], argv[2], argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    res = session.query(State).order_by(State.id).first()
    if (res is None):
        print("Nothing")
    else:
        print(f"{res.id}: {res.name}")
