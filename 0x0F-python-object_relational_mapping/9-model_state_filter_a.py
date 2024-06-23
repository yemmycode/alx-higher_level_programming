#!/usr/bin/python3
"""
This script lists all State objects that contain the letter 'a' from the `hbtn_0e_6_usa` database.
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Connect to the database and retrieve all State objects containing the letter 'a'.
    """

    db_uri = f'mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}'
    engine = create_engine(db_uri)
    Session = sessionmaker(bind=engine)
    session = Session()

    states_with_a = session.query(State).filter(State.name.contains('a')).all()
    for state in states_with_a:
        print(f'{state.id}: {state.name}')
