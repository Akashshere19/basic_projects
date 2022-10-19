Name  = input('Enter your username :')
Password  = input ('Enter your  password :')

import mysql.connector
data = mysql.connector.connect(host='localhost',user='root',password='akash19',database="testdb")
cursor = data.cursor()

sql = "insert into employ values(5,'archana','testing',23.9);"
cursor.execute(sql)
data.commit()
data.close()
print("Record Added................")