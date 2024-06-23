#!/usr/bin/python3
"""
This script takes an argument and
displays all values in the states table
where `name` matches the argument
from the database `hbtn_0e_0_usa`.
"""

import MySQLdb
import sys

if __name__ == '__main__':
    """
    Connect to the database and fetch states
    matching the provided name.
    """
    connection = MySQLdb.connect(host="localhost", user=sys.argv[1], port=3306,
                                 passwd=sys.argv[2], db=sys.argv[3])

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY '{}' ORDER BY id ASC".format(sys.argv[4]))
    rows = cursor.fetchall()

    for row in rows:
        print(row)
