#!/usr/bin/python3
"""
This script accesses a MySQL database
and retrieves all states from it.
"""

import MySQLdb
import sys

if __name__ == '__main__':
    """
    Connect to the MySQL database using provided credentials
    and fetch all states from the 'states' table.
    """
    connection = MySQLdb.connect(host="127.0.0.1", user=sys.argv[1], port=3306,
                                 passwd=sys.argv[2], db=sys.argv[3])

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM states")
    rows = cursor.fetchall()

    for row in rows:
        print(row)
