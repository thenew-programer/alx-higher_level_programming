#!/usr/bin/python3
"""
script to Lists all states from the database hbtn_0e_0_usa
"""
import sys
import MySQLdb

def main():
    db = MySQLdb.connect(user=sys.argv[1], passwd=sys.argv[2],
                         db=sys.argv[3], port=3306)

    cur = db.cursor()
    cur.execute("SELECT * FROM states;")
    states = cur.fetchall()

    for state in states:
        print(state)

if __name__ == '__main__':
    main()
