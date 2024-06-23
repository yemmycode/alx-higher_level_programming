#!/usr/bin/python3
"""
This script updates the name of a State object
in the database `hbtn_0e_6_usa`.
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Update a State object in the database.
    """

    db_uri = f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}"
    engine = create_engine(db_uri)
    Session = sessionmaker(bind=engine)

    session = Session()

    state_to_update = session.query(State).filter(State.id == '2').first()
    state_to_update.name = 'New Mexico'

    session.commit()

    session.close()
