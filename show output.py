'''import mysql.connector
data = mysql.connector.connect(host='localhost',user='root',password='akash19',database="testdb")

sql = "select * from company_employee;"
cursor = data.cursor()
cursor.execute(sql)
result=cursor.fetchall()

print("show data")
data.close()
for row in result:
        print("Id = ", row[0], )
        print("Name = ", row[1])
        print("dept  = ", row[2])
        print("salary  = ", row[3], "\n")
'''
'''
import mysql.connector
db = mysql.connector(host='localhost',user='root',password='akash19',database='testdb')
'''

import cx_Oracle


con = cx_Oracle.connect('akash/Akash19@localhost')
cur = con.cursor()
try:
    sqlstr= 'create table dept(deptno number(4),dname varchar2(20),loc varchar2(20)'
    cur.execute(sqlstr)
    con.commit()
    print('table create')
except:
        print('table not created')
        
finally:
        cur.close()
        con.close()

                     
