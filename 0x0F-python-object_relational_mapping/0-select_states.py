#!/usr/bin/python3
import MySQLdb
import sys

"""
Module script that list states
"""


def list_states(mysql_username, mysql_password, db_name):
    """
    List all states from
    the database.
    """
    db = MySQLdb.connect(host="localhost", port=3306, user=mysql_username,
                         passwd=mysql_password, db=db_name)
    cur = db.cursor()
    cur.execute("SELECT * FROM states ORDER BY id ASC")
    rows = cur.fetchall()
    for row in rows:
        print(row)
    cur.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) == 4:
        mysql_username = sys.argv[1]
        mysql_password = sys.argv[2]
        db_name = sys.argv[3]
        list_states(mysql_username, mysql_password, db_name)
