#!/usr/bin/python3
"""
Script to select all states from the database.
"""

import sys
import MySQLdb


def main(username, password, database):
    """
    Function to select all states from database hbtn_0e_0_usa
    where name starts with N.
    """

    db = MySQLdb.connect(
            host="localhost",
            port=3306,
            user=username,
            passwd=password,
            db=database)

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")

    rows = cursor.fetchall()

    i = 0
    for row in rows:
        print("{}, {}".format(i, row))
        i++

    cursor.close()
    db.close()


if __name__ == "__main__":
    username, password, database = sys.argv[1:]
    main(username, password, database)
