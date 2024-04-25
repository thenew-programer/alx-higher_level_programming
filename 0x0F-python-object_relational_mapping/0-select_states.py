#!/usr/bin/python3
'''Select sql statement using ORM'''
import sys
import MySQLdb

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print(len(sys.argv))
    else:
        print(len(sys.argv))
        username = sys.argv[1]
        password = sys.argv[2]
        db_name = sys.argv[3]

        conn = MySQLdb.connect(host="localhost", port=3306, user=username,
                               passwd=password, db=db_name, charset="utf8")
        cur = conn.cursor()
        # HERE I have to know SQL to grab all states in my database
        cur.execute("SELECT * FROM states ORDER BY id ASC")
        query_rows = cur.fetchall()
        for row in query_rows:
            print(f'({row.id}, {row.name})')
        cur.close()
        conn.close()
