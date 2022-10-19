import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost',user='root',password='akash19',database="testdb")
    cursor = connection.cursor()

    print("Before updating a record ")
    sql_select_query = """select * from employ where id = 13"""
    cursor.execute(sql_select_query)
    record = cursor.fetchone()
    print(record)

    # Update single record now
    sql_update_query = """Update employ set salary = 7000 where id = 13"""
    cursor.execute(sql_update_query)
    connection.commit()
    print("Record Updated successfully ")

    print("After updating record ")
    cursor.execute(sql_select_query)
    record = cursor.fetchone()
    print(record)

except mysql.connector.Error as error:
    print("Failed to update table record: {}".format(error))
finally:
    if connection.is_connected():
        connection.close()
        print("MySQL connection is closed")
