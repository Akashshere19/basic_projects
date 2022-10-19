import mysql.connector
from mysql.connector.errors import Error
host="localhost"
user="root"
password="akash19"
database="testdb"
try:
    connection = mysql.connector.connect(host='localhost',user='root',password='akash19',database="testdb")
    inserttable = "insert into employ values(5,'akshay','testing',23.9);"
    cursor=connection.cursor()
    #dbcreate="CREATE DATABASE testdb"
   # cursor.execute(dbcreate)
    
   # inserttable="INSERT INTO employ VALUES(4,'rohit','service',29000);"
    cursor.execute(inserttable)
    connection.commit()
    print("DONE")       
except Error as e:
    print("error occured",e)
finally:
     if(connection.is_connected()):
       cursor.close()
       connection.close()
       print("connection is closed") 