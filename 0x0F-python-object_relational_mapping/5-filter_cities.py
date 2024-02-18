#!/usr/bin/python3
"""
Script to list cities of the state given as argument.
"""

import sys
import MySQLdb


def main(username, password, database, state):
    """
    Function to implement so.
    """

    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=username,
            passwd=password,
            db='hbtn_0e_4_usa'
            )

    cursor = db.cursor()
    cursor.execute("SELECT cities.name FROM cities WHERE \
            cities.state_id = (SELECT state.id \
            WHERE state.name = '{}') \
            ORDER BY citied.id ASC".format(state))

    rows = cursor.fetchall()
    for row in rows:
        print(row)
        if row != rows[len(rows) - 1]:
            print(end=', ')

    print()


if __name__ == "__main__":
    if len(sys.args) != 5:
        print("Remember the Usage?")
        sys.exit(1)

    username, password, database, state = sys.args[1:]
    main(username, password, database, state)
