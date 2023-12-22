#!/usr/bin/python3
"""
Prints the State object with a specific name from the database
hbtn_0e_6_usa.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State
import sys


def print_state_by_name(mysql_username, mysql_pswd, db_name, state_name):
    """
    Print the State object with the specified name from the database.
    """
    engine = create_engine(
        f'mysql+mysqldb://{mysql_username}:{mysql_pswd}@localhost/{db_name}'
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    state = session.query(State).filter(State.name == state_name).first()

    if state:
        print(f"{state.id}")
    else:
        print("Not found")

    session.close()

if __name__ == "__main__":
    if len(sys.argv) == 5:
        mysql_username = sys.argv[1]
        mysql_pswd = sys.argv[2]
        db_name = sys.argv[3]
        state_name = sys.argv[4]
        print_state_by_name(mysql_username, mysql_pswd, db_name, state_name)
