#!/usr/bin/python3
"""
This script defines a City class
to work with SQLAlchemy ORM.
"""

from model_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship

class City(Base):
    """
    City class for SQLAlchemy ORM.

    Attributes:
        __tablename__ (str): The table name of the class.
        id (int): The primary key of the City table.
        name (str): The name of the city.
        state_id (int): The foreign key referencing the states table.
        state (relationship): Relationship to the State object.
    """

    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
    state = relationship('State')

    def __repr__(self):
        return f"City(id={self.id}, name={self.name}, state_id={self.state_id})"
