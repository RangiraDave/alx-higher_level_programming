#!/usr/bin/python3

import sys
import MySQLdb

def main(username, password, database):
    """
    Function to select all states from database hbtn_0e_0_usa
    where name starts with N.
    """

    db = MySQLdb.connect(host="localhost", port=3306, user=username, passwd=password, db=database)

    cursor = db.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id")

    rows = cursor.fetchall()

    for row in rows:
        print(row)

    cursor.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./0-select_states.py <username> <password> <database>")
        sys.exit(1)

    username, password, database = sys.argv[1:]

    main(username, password, database)
