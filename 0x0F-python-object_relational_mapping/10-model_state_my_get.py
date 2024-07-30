#!/usr/bin/python3
"""
This script retrieves and prints the ID of a State object
matching the specified name from the database `hbtn_0e_6_usa`.
"""

import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Access the database and fetch a state
    based on the provided arguments.
    """

    db_uri = f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost:3306/{sys.argv[3]}"
    engine = create_engine(db_uri)
    Session = sessionmaker(bind=engine)

    session = Session()

    state_name = sys.argv[4]
    state_instance = session.query(State).filter(State.name == state_name).first()

    if state_instance:
        print(state_instance.id)
    else:
        print("Not found")
