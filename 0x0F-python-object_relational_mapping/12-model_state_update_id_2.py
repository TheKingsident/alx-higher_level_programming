#!/usr/bin/python3
"""
Changes name of the State object with id = 2 to 'New Mexico'
in the database hbtn_0e_6_usa.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import State
import sys


def update_state(mysql_username, mysql_pswd, db_name):
    """
    Change the name of the State with id = 2 to 'New Mexico'.
    """
    engine = create_engine(
        f'mysql+mysqldb://{mysql_username}:{mysql_pswd}@localhost/{db_name}'
    )

    Session = sessionmaker(bind=engine)
    session = Session()

    # Find the state with id = 2
    state_to_update = session.query(State).filter(State.id == 2).first()

    if state_to_update:
        # Update the state's name
        state_to_update.name = 'New Mexico'
        session.commit()

    session.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        mysql_username = sys.argv[1]
        mysql_pswd = sys.argv[2]
        db_name = sys.argv[3]
        update_state(mysql_username, mysql_pswd, db_name)
