#!/usr/bin/python3
"""
Script to list cities of the state given as argument.
"""

import MySQLdb


def main(username, password, database, state):
    """
    Function to implement so.
    """

    db = MySQLdb.connect(
            host = 'localhost',
            port = 3306,
            user = username,
            passwd = password,
            db = 'hbtn_0e_4_usa'
            )

    cursor = db.cursor()
    cursor.execute("SELECT cities.name FROM cities \
            INNER OUTER states ON cities.state_id = state.id \
            WHERE state.name = '{}'
            ORDER BY citied.id ASC".format(state))

    rows = cursor.fetchall()
    i=0
    for cit in rows:
        i += 1
        if i != len(rows) - 2:
            print(cit, end=', ')

        print(cit)
