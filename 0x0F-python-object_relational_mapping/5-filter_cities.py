#!/usr/bin/python3
'''
Write a script that lists all cities of state
from the database hbtn_0e_4_usa
using state name given by the user
'''

import MySQLdb
from sys import argv

if __name__ == "__main__":
    '''
    - Your script should take 4 arguments: mysql username,
        mysql password, database name and state name (SQL injection free!)
    - You must use the module MySQLdb (import MySQLdb)
    - Your script should connect to a MySQL server running
        on localhost at port 3306
    - Results must be sorted in ascending order by cities.id
    - You can use only execute() once
    - The results must be displayed as they are in the example below
    - Your code should not be executed when imported
    '''
    conn = MySQLdb.connect(host="localhost", user=argv[1], port=3306,
                           passwd=argv[2], db=argv[3])

    with conn.cursor() as cur:
        cur.execute("""
            SELECT
                cities.id, cities.name, states.name
            FROM
                cities
            JOIN
                states
            ON
                cities.state_id = states.id
            WHERE
                states.name LIKE BINARY %s
            ORDER BY
                cities.id ASC
        """, argv[4])

        records = cur.fetchall()

    if records is not None:
        for row in records:
            print(row)
