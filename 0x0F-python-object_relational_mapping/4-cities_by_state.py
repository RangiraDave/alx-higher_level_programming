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

    try:
        db = MySQLdb.connect(
                host='localhost',
                port=3306,
                user=username,
                passwd=password,
                db=database
                )
        cursor = db.cursor()
        cursor.execute("SELECT * FROM cities ORDER BY id")
        rows = cursor.fetchall()

        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print(f"Error: {e}")

    finally:
        if cursor:
            cursor.close()
        if db:
            db.close()


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: ./4-cities_by_states.py <username> \
                <password> <database>")
        sys.exit(1)

    username, password, database = sys.argv[1:]
    main(username, password, database)
