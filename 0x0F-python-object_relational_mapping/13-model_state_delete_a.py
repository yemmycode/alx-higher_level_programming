#!/usr/bin/python3
"""
This script deletes all State objects
with a name containing the letter `a`
from the database `hbtn_0e_6_usa`.
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Deletes State objects from the database.
    """

    db_uri = f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}"
    
    engine = create_engine(db_uri)
    
    Session = sessionmaker(bind=engine)
    
    session = Session()
    
    for state in session.query(State).filter(State.name.contains('a')):
        session.delete(state)
    
    session.commit()
    
    session.close()
