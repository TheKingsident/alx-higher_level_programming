#!/usr/bin/python3
"""
Adds State object to the database hbtn_0e_6_usa
and prints the new state's ID.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State
import sys


def add_louisiana(mysql_username, mysql_pswd, db_name):
    """
    Add the State 'Louisiana' to the database and print its ID.
    """
    engine = create_engine(
        f'mysql+mysqldb://{mysql_username}:{mysql_pswd}@localhost/{db_name}'
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    new_state = State(name='Louisiana')
    session.add(new_state)
    session.commit()

    print(f"{new_state.id}")

    session.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        mysql_username = sys.argv[1]
        mysql_pswd = sys.argv[2]
        db_name = sys.argv[3]
        add_louisiana(mysql_username, mysql_pswd, db_name)
