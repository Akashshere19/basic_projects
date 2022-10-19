import mysql.connector
import datetime
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
        query = "select * from persons"
        cursor=conn.cursor()
        cursor.execute(query)
        emp_list = []

        for rec in cursor:
            emp_list.append(Employee(*rec))

    except mysql.connector.Error as err:
         if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
             print("Name or Passward error ! :(")
         elif err.errno == errorcode.ER_BAD_DB_ERROR:
             print("Database Doesn't exist!")
         else:
             print(err)
    else:
         cursor.close()
         conn.close()
    finally:
         print('Transaction backup has been taken successfully')
         print('Shutting down the system')
