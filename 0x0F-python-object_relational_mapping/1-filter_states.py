#!/usr/bin/python3
"""
This script lists all states from the
database `hbtn_0e_0_usa` where the state
name starts with the letter 'N'.
"""

import MySQLdb
import sys

if __name__ == '__main__':
    """
    Connect to the database and retrieve states
    with names starting with 'N'.
    """
    connection = MySQLdb.connect(host="localhost", user=sys.argv[1], port=3306,
                                 passwd=sys.argv[2], db=sys.argv[3])

    cursor = connection.cursor()
    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY id ASC")
    rows = cursor.fetchall()

    for row in rows:
        print(row)
