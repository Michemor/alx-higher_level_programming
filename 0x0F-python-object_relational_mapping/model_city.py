#!/usr/bin/python3
""" creates a city table """

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State
from sqlalchemy.orm import relationship


class City(Base):
    """
    Creates a city table:
        id (int): unique indetifier for each object
        name(str): name for each city
    """
    __tablename__ = "cities"

    id = Column("id", Integer, autoincrement=True, unique=True,
                nullable=False, primary_key=True)
    name = Column("name", String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
