import psycopg2

try:
    # connect to the PostgreSQL server
    conn = psycopg2.connect(host="postgres",
        port= '5432',
        database="appstore", 
        user="postgres", 
        password="postgres",
        sslmode = "require",
        sslcert = "/ramfs/secrets/zoomdatapg/zoomdatapgusr.cert.pem",
        sslkey="/ramfs/secrets/zoomdatapg/zoomdatapgusr.key.pem"
    )

    # create a cursor
    cur = conn.cursor()

    # # Execute a sql
    # cur.execute('SELECT version()')

    # # display the PostgreSQL database server version
    # version = cur.fetchall()
    # print(version)

    # select data
    print("Select all data in data_dig.tbl_stream_history")
    cur.execute("SELECT * from data_dig.tbl_stream_history;")
    data = cur.fetchall()
    print(data)

    # close the communication with the PostgreSQL
    cur.close()
except Exception as e:
    print('Unable to connect %s' % str(e))

finally:
    if conn is not None:
        conn.close()