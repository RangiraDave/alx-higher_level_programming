#!/usr/bin/python3
"""
The script that lists all State objects that contain the letter a.
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    """this is makes main"""
    username = argv[1]
    password = argv[2]
    database = argv[3]
    host = 'localhost'
    port = 3306
    connection = f'mysql+mysqldb://{username}:\
        {password}@{host}:{port}/{database}'

    engine = create_engine(connection)

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State)\
        .filter(State.name.like('%a%')).order_by(State.id.asc()).all()

    for state in states:
        print("{}: {}".format(state.id, state.name))
