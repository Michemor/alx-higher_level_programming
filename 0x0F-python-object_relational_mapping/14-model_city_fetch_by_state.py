#!/usr/bin/python3
"""
prints all City objects from the database hbtn_0e_14_usa
"""

from model_city import City
from model_state import State
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
import sys

if __name__ == "__main__":

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
                sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    sess = Session()
    res = sess.query(State.name, City.id, City.name).filter(
                    City.state_id == State.id).order_by(City.id)
    for (state_name, city_id, city_name) in res:
        print(f"{state_name}: ({city_id}) {city_name}")
