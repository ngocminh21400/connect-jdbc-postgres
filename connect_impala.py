from impala.dbapi import connect
conn = connect('hadoop-data.default.svc.cluster.local', port=21050)
cursor = conn.cursor()
cursor.execute('SHOW DATABASES')
cursor.fetchall()
print(cursor)