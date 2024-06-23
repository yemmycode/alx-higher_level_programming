#!/usr/bin/python3
"""
This script takes the name of a state as an argument and lists all cities of that state from the `hbtn_0e_4_usa` database.
"""

import MySQLdb
import sys

if __name__ == '__main__':
    """
    Connect to the database and retrieve cities for the specified state.
    """

    db = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
        port=3306
    )

    with db.cursor() as cursor:
        cursor.execute("""
            SELECT
                cities.id, cities.name
            FROM
                cities
            JOIN
                states ON cities.state_id = states.id
            WHERE
                states.name = %(state_name)s
            ORDER BY
                cities.id ASC
        """, {
            'state_name': sys.argv[4]
        })

        cities = cursor.fetchall()

    if cities:
        print(", ".join(city[1] for city in cities))

