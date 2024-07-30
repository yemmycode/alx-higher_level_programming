#!/usr/bin/python3
"""
This script inserts the State object
'Louisiana' into the database 'hbtn_0e_6_usa'.
"""

from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access the database and add the 'Louisiana' state
    to the database.
    """

    db_uri = f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}"
    engine = create_engine(db_uri)
    Session = sessionmaker(bind=engine)

    session = Session()

    lou_state = State(name='Louisiana')

    session.add(lou_state)
    session.commit()

    print(lou_state.id)

    session.close()
