#!/usr/bin/python3
"""
Displays all values in the states table of hbtn_0e_0_usa
where name matches the argument but safe from MySQL injections!
"""
import MySQLdb
from sys import argv

if __name__ == '__main__':
    try:
        db = MySQLdb.connect(
            host='localhost',
            user=argv[1],
            passwd=argv[2],
            db=argv[3],
            port=3306
        )

        cursor = db.cursor()

        cursor.execute("SELECT id, name FROM states \
        WHERE name LIKE %s \
        ORDER BY states.id ASC;", (argv[4],))

        r = cursor.fetchall()
        for row in r:
            print(row)
        cursor.close()
    except Exception as err:
        print(err)
        pass
