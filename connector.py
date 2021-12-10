#!/usr/bin/python3
import psycopg2

try:
    # connect to the PostgreSQL server
    conn = psycopg2.connect(host="10.96.191.228",database="appstore", user="postgres", password="postgres")

    # create a cursor
    cur = conn.cursor()

    # Execute a sql
    cur.execute('SELECT version()')

    # display the PostgreSQL database server version
    version = cur.fetchone()
    print(version)

    # close the communication with the PostgreSQL
    cur.close()
except Exception as e:
    print('Unable to connect %s' % str(e))

finally:
    if conn is not None:
        conn.close()