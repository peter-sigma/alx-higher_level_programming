#!/usr/bin/python3
""" list all states """
import MySQLdb
import sys

if __name__ == "__main__":
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
            passwd=sys.argv[2], db=sys.argv[3], port=3306)
    mycursor = db.cursor()
    mycursor.execute("""SELECT * FROM states WHERE name LIKE BINARY 'N%' ORDER BY states.id""")
    rows = mycursor.fetchall()
    for r in rows:
        print(r)
    mycursor.close()
    db.close()
