#!/usr/bin/python3
"""
This script takes an argument and displays all values in the states
table where `name` matches the argument from the database `hbtn_0e_0_usa`.
This version of the script is safe from MySQL injections.
"""

import MySQLdb
import sys

if __name__ == '__main__':
    """
    Connect to the database and fetch states matching the provided name.
    """

    connection = MySQLdb.connect(host="localhost", user=sys.argv[1], port=3306,
                                 passwd=sys.argv[2], db=sys.argv[3])

    with connection.cursor() as cursor:
        query = """
            SELECT
                *
            FROM
                states
            WHERE
                name LIKE BINARY %(name)s
            ORDER BY
                id ASC
        """
        cursor.execute(query, {'name': sys.argv[4]})
        rows = cursor.fetchall()

    for row in rows:
        print(row)
