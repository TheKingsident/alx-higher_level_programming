#!/usr/bin/python3
""" Module script that list states """
import MySQLdb
import sys


def search_states():
    """ List all states from the database. """
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3])

    nameSch = sys.argv[4]
    query = "SELECT * FROM {} WHERE name = %s ORDER BY id ASC".format('states')
    cur = db.cursor()
    cur.execute(query, (nameSch,))
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    search_states()
