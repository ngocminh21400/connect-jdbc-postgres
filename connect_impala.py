from impala.dbapi import connect
import ssl
import os
# impala://hadoop-data.default.svc.cluster.local:21050/default;principal=impala/hadoop-data.default.svc.cluster.local@cluster.local

conn = connect(host='hadoop-data.default.svc.cluster.local', port=21050, use_ssl = True, database = 'testdb', user = 'impala', kerberos_service_name = 'impala', auth_mechanism = 'GSSAPI')
cursor = conn.cursor()
cursor.execute('SHOW DATABASES;')
databases = cursor.fetchall()
print(databases)