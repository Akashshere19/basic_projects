import mysql.connector
conn = mysql.connector.connect(host='localhost',user='root',password='akash19',database="testdb")
cursor = conn.cursor()
query = "create table company_employee ( id int(6), name char(30), dept char(30), salary float(7,2));"
cursor.execute(query)
conn.close()
print('success')