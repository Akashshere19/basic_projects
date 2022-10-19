import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost',user='root',password='akash19',database="testdb")

    mySql_insert_query = "insert into employ values(5,'archana','testing',23.9);"

    cursor = connection.cursor()
    cursor.execute(mySql_insert_query)
    connection.commit()
    print(cursor.rowcount, "Record inserted successfully into Laptop table")
    cursor.close()

except mysql.connector.Error as error:
    print("Failed to insert record into Laptop table {}".format(error))

finally:
    if connection.is_connected():
        connection.close()
        print("MySQL connection is closed")
