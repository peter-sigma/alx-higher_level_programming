#!/usr/bin/python3
""" List all states from the database hbtn_0e_0_usa """
import MySQLdb
from sys import argv

if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], db=argv[3])

    c = db.cursor()
    c.execute("SELECT * FROM states")

    r = c.fetchall()
    for i in r:
        print(i)
    c.close()
    db.close()
