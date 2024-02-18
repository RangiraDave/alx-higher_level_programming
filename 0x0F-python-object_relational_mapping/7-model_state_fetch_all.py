#!/usr/bin/python3
"""
Function to fetch all states
"""

import sys
# import sqlalchemy
from sqlalchemy import create_engine, Column, Integer, String, MetaData
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


def main(username, password, database):
    """
    Function to handle the logic.
    """

    host = "localhost"
    connection = f"mysql+mysqldb://{username}:{password}@{host}\
            :3306/{database}"

    engine = create_engine(connection)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State).order_by(State.id.asc()).all()
    for state in states:
        print("{}: {}".format(state.id, state.name))


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./script <username> <password> <database>")
        sys.exit(1)

    username, password, database = sys.argv[1:]
    main(username, password, database)
