#!/usr/bin/python3
"""
write a script that takes in arguments and
displays all values in the states table of
hbtn_0e_0_usa where name matches the
argument. But this time, write one that is
safe from MySQL injections!
"""

import MySQLdb
from sys import argv

if __name__ == "__main__":
    """
    connect to db, construct the query
    and run the sql query
    """
    state_name = {'name': argv[4]}
    conn = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                           passwd=argv[2], db=argv[3])
    with conn.cursor() as cur:
        cur.execute("""
            SELECT
                *
            FROM
                states
            WHERE
                name LIKE BINARY %(name)s
            ORDER BY
                states.id ASC
        """, state_name)

        rows = cur.fetchall()

        if rows is not None:
            for row in rows:
                print(row)
