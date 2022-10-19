import mysql.connector
from mysql.connector.errors import Error
host="localhost"
user="root"
password="akash19"
database="testdb"
try:
    connection=mysql.connector.connect(host=host,user=user,password=password,database=database)
    cursor=connection.cursor()
    #dbcreate="CREATE DATABASE testdb"
   # cursor.execute(dbcreate)
    
    inserttable="""INSERT INTO employ VALUES(18,'rohitkumar','service',22000),
                 (17,'akshata thakur','service',22000),
                  (116,'divya sharma','service',22000);"""
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
