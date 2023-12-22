#!/usr/bin/python3
"""
Lists all State objects, and corresponding City objects
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, joinedload
from relationship_state import State
from relationship_city import City  # Import City at the beginning
import sys


def list_states_and_cities(mysql_username, mysql_pswd, db_name):
    """
    Lists all State objects and their corresponding City objects.
    """
    engine = create_engine(
        f'mysql+mysqldb://{mysql_username}:{mysql_pswd}@localhost/{db_name}'
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    # Querying all states with their related cities
    states = session.query(State).options(joinedload(State.cities)).order_by(
        State.id, City.id).all()

    for state in states:
        print(f"{state.id}: {state.name}")
        for city in state.cities:
            print(f"\t{city.id}: {city.name}")

    session.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        mysql_username = sys.argv[1]
        mysql_pswd = sys.argv[2]
        db_name = sys.argv[3]
        list_states_and_cities(mysql_username, mysql_pswd, db_name)
