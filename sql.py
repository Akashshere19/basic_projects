'''from typing import Optional
from sqlmodel import Field, SQLModel

class Hero(SQLModel,table=True):
    id:Optional[int] = Field(default =None,primary_key =True)
    name: str
    secret_name: str
    age: Optional[int] = None
'''
'''
import mysql.connector
conn = mysql.connector.connect(host='localhost',user='root',password='akash19',database="testdb")
cursor = conn.cursor()
query = "create table company_employee ( id int(6), name char(30), dept char(30), salary float(7,2));"
cursor.execute(query)
conn.close()
print('success')
'''

'''
# prog for  create student table and insert data
# import sql connector
import mysql.connector
#connect with server
dataBase = mysql.connector.connect(
  host ="localhost",
  user ="root",
  passwd ="akash19",
)
 
# preparing a cursor object
cursorObject = dataBase.cursor()
 
# creating database
cursorObject.execute("CREATE DATABASE Studentdb1")
print('database create')

dataBase = mysql.connector.connect(
  host ="localhost",
  user ="root",
  passwd ="akash19",
  db ="Studentdb1"
)

# create cursor for table
cursorObject = dataBase.cursor()
#ceate STUDENT table
table = "create table STUDENT (Student_No int(5), Student_Name char(50), Student_DOB Date, Student_DOJ Date);"
cursorObject.execute(table)

# Insert data into table
sql = """INSERT INTO Student (Student_No, Student_Name, Student_DOB, Student_DOJ) VALUES (1,'shree','1998-05-21','2022-05-1'),
                                                                                    (2,'sham','1998-05-21','2022-05-1');"""
cursorObject.execute(sql)
 

#Delete data row 
#sql = "DELETE FROM Student WHERE Student_name ='shree';"

#cursorObject.execute(sql)

# displaying tables details
sql = "select * from student;"
cursorObject.execute(sql)


result=cursorObject.fetchall()
for row in result:
        print("student_no = ", row[0])
        print("student_Name = ", row[1])
        print("Student_DOB  = ", row[2])
        print("Student_DOJ = ", row[3], "\n")
print(result)
#data.commit()        
dataBase.commit()        
dataBase.close()
print('Success..!')'''
'''

import datetime
import mysql.connector
from mysql.connector import errorcode

emp_list = []

class Employee(object):
    def __init__(self,_id,_dob,_fname,_lname,_gender,_doj):
        self.empId= _id
        self.dob = _dob
        self.FirstName = _fname
        self.LastName = _lname
        self.gender = _gender
        self.DoJ = _doj
        
    def __str__(self):
        return '{},{},{},{},{}'.format(self.empId,self.dob,self.FirstName,
                                       self.LastName,self.gender,self.DoJ)

    def __repr__(self):
        return 'employee({},{},{},{},{},{})'.format(self.empId,self.dob,self.FirstName,
                                       self.LastName,self.gender,self.DoJ)

if __name__ == '__main__':
    
    try:
        conn = mysql.connector.connect(user='root',password='akash19',host='localhost',database='employee')
        query = "select * from person"
        cursor.execute(query)
        emp_list = []

        for rec in cursor:
            emp_list.append(employee(*rec))

    except mysql.connector.Error as err:
         if err.errno == errrorcode.Er_Access_DENIND_error:
             print("Name or Passward error ! :(")
         elif err.errno == errorcode.ER_BD_DB_ERROR:
             print("Database Doesn't exist!")
         else:
             print(err)
    else:
         cursor.close()
         conn.close()
    finally:
         print('Transaction backup has been taken successfully')
         print('Shutting down the system')
'''

import mysql.connector
conn = mysql.connector.connect(host='localhost',user='root',password='akash19',database="testdb")
cursor = conn.cursor()
query = "create table company_employee ( id int(6), name char(30), dept char(30), salary float(7,2));"
cursor.execute(query)
conn.close()
print('success')



             

