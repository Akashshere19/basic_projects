import mysql.connector
conn = mysql.connector.connect(host='localhost',user='root',password='akash19')
cursor = conn.cursor()
query = "DROP TABLE IF EXISTS EMPLOYEES;"
query = "CREATE DATABASE Employee"
cursor.execute(query)
conn.close()
print('success')