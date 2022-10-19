import mysql.connector
data = mysql.connector.connect(host='localhost',user='root',password='akash19',database="testdb")

sql = "insert into company_employee(id,name,dept,salary) values(2,'shoham','testing',13.00);"
cursor = data.cursor()
cursor.execute(sql)
data.commit()
data.close()
print("insert data")
