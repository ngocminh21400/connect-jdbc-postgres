from impala.dbapi import connect

conn = connect(host='hadoop-data.default.svc.cluster.local', port=21050)
cursor = conn.cursor()
cursor.execute('SHOW DATABASES;')
# print cursor.description  # prints the result set's schema
results = cursor.fetchall()
print(results)