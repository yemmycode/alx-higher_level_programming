#!/usr/bin/python3
"""
Defines a State class and a Base class to interact with MySQLAlchemy ORM.
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

# Declare a base class for SQLAlchemy ORM
Base = declarative_base()

# Define a State class that inherits from the Base class
class State(Base):
    """Represents a state entity in the database."""
    
    __tablename__ = 'states'  

    id = Column(Integer, primary_key=True)  
    name = Column(String(128), nullable=False) 
    cities = relationship("City", backref="state", cascade="all, delete")  

    def __repr__(self):
        return f"<State(id={self.id}, name='{self.name}')>"
