#!/usr/bin/python3
"""
This script defines the City class for MySQLAlchemy ORM.
"""

from relationship_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """
    City class for ORM

    Attributes:
        __tablename__ (str): Name of the table in the database
        id (int): Primary key id of the city
        name (str): Name of the city
        state_id (int): Foreign key referencing the state id

    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
