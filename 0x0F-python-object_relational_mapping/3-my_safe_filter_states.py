#!/usr/bin/python3
"""
This script that takes in an argument and displays
all values in the states table of hbtn_0e_0_usa
where name matches the argument.
"""

import MySQLdb
from sys import argv

for i in range(len(argv)):
    print(argv[i])

if __name__ == "__main__":
    """
    connect to db, construct the query
    and run the sql query
    """
    query = "SELECT * FROM states WHERE name = '%s' ORDER BY states.id ASC"
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])
    cur = conn.cursor()
    cur.execute(query, (argv[4],))
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
