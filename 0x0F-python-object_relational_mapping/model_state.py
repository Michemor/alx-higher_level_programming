#!/usr/bin/python3
""" uses python ORM to store data in database without direct SQL queries"""

from sqlalchemy import Column, Integer, create_engine, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """ defines a state table and its attributes """

    __tablename__ = "states"

    id = Column("id", Integer, primary_key=True, autoincrement=True,
                nullable=False, unique=True)
    name = Column("name", String(128), nullable=False)
