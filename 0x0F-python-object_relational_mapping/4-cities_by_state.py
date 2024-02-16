#!/usr/bin/python3
"""
Script to select all cities in hbtn_0e_4_usa
"""
import sys
import MySQLdb


def main(username, password, database):
    """
    Function to handle the execution of the queries.
    """

    db = MySQLdb.connect(
            host='localhost',
            port=3306,
            user=username,
            passwd=password,
            db=database
            )
    cursor = db.cursor()
    cursor.execute("SELECT cities.id, cities.name, states.name \
            FROM cities JOIN states ON cities.state_id = \
            states.id ORDER BY cities.id ASC")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    username, password, database = sys.argv[1:]
    main(username, password, database)
