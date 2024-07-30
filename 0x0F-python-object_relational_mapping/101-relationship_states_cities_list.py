#!/usr/bin/python3
"""
Lists all State objects and corresponding City objects in the database.
"""
import sys
from relationship_state import Base, State
from relationship_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    db_uri = f"mysql+mysqldb://{sys.argv[1]}:{sys.argv[2]}@localhost:3306/{sys.argv[3]}"
    engine = create_engine(db_uri, pool_pre_ping=True)
    
    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    
    session = Session()

    states_with_cities = session.query(State).outerjoin(City).order_by(State.id, City.id).all()

    for state in states_with_cities:
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"    {city.id}: {city.name}")

    session.close()
