#!/usr/bin/python3
"""
Prints the first State object from the database hbtn_0e_6_usa.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State
import sys


def print_states_with_a(mysql_username, mysql_pswd, db_name):
    """
    Print the first State object from the database.
    """
    engine = create_engine(
        f'mysql+mysqldb://{mysql_username}:{mysql_pswd}@localhost/{db_name}'
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).filter(State.name.like('%a%')).order_by(
        State.id)

    for state in states:
        print(f"{state.id}: {state.name}")

    session.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        mysql_username = sys.argv[1]
        mysql_pswd = sys.argv[2]
        db_name = sys.argv[3]
        print_states_with_a(mysql_username, mysql_pswd, db_name)
