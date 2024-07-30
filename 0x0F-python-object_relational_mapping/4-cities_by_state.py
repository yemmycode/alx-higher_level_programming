#!/usr/bin/python3
"""
This script lists all cities from
the database `hbtn_0e_4_usa`.
"""

import MySQLdb
import sys

if __name__ == '__main__':
    """
    Connect to the database and retrieve all cities.
    """

    connection = MySQLdb.connect(host="localhost", user=sys.argv[1], port=3306,
                                 passwd=sys.argv[2], db=sys.argv[3])

    with connection.cursor() as cursor:
        cursor.execute("""
            SELECT
                cities.id, cities.name, states.name
            FROM
                cities
            JOIN
                states ON cities.state_id = states.id
            ORDER BY
                cities.id ASC
        """)

        rows = cursor.fetchall()

    for row in rows:
        print(row)
