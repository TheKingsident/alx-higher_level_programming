#!/usr/bin/python3
""" Module script that list states """
import MySQLdb
import sys


def list_states():
    """ List all states from the database. """
    db = MySQLdb.connect(host="localhost", port=3306, user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute(
        "SELECT * FROM states WHERE LOWER(name) LIKE 'n%' ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    list_states()
