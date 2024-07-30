#!/usr/bin/python3
"""
Prints all City objects from the database `hbtn_0e_14_usa`.
"""

from sys import argv
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

if __name__ == "__main__":
    """
    Accesses the database and retrieves cities.
    """

    db_uri = f"mysql+mysqldb://{argv[1]}:{argv[2]}@localhost:3306/{argv[3]}"
    engine = create_engine(db_uri)
    Base.metadata.create_all(engine)
    
    Session = sessionmaker(bind=engine)
    
    session = Session()
    
    cal_state = State(name='California')
    
    sfr_city = City(name='San Francisco')
    cal_state.cities.append(sfr_city)
    
    session.add(cal_state)
    session.commit()
    session.close()
