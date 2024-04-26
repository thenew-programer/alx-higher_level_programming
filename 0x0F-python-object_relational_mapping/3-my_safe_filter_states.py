#!/usr/bin/python3
"""
This script that takes in an argument and displays
all values in the states table of hbtn_0e_0_usa
where name matches the argument.
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """
    connect to db, construct the query
    and run the sql query
    """
    state_name = {'name': argv[4]}
    query = "SELECT * FROM states WHERE name LIKE BINARY %(name) ORDER BY states.id ASC"
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    cur.execute(query, state_name)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
