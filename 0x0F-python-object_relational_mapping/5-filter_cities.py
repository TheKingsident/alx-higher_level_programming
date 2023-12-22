#!/usr/bin/python3
""" Module script that lists cities of a specific state """
import MySQLdb
import sys


def list_cities_of_state(mysql_username, mysql_password, db_name, state_name):
    """ List all cities of a specific state from the database. """
    db = MySQLdb.connect(host="localhost",
                         port=3306,
                         user=mysql_username,
                         passwd=mysql_password,
                         db=db_name)

    cur = db.cursor()
    query = ("SELECT cities.name FROM cities "
             "JOIN states ON cities.state_id = states.id "
             "WHERE states.name = %s ORDER BY cities.id ASC")
    cur.execute(query, (state_name,))
    rows = cur.fetchall()
    cities = ', '.join([row[0] for row in rows])
    print(cities)

    cur.close()
    db.close()


if __name__ == "__main__":
    if len(sys.argv) == 5:
        mysql_username = sys.argv[1]
        mysql_password = sys.argv[2]
        db_name = sys.argv[3]
        state_name = sys.argv[4]
        list_cities_of_state(mysql_username,
                             mysql_password,
                             db_name,
                             state_name)
