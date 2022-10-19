import mysql.connector
con=mysql.connector.connect(user = 'root',
                            password='akash19',
                            host = 'localhost',
                           database='employees')
cur=con.cursor()
#query = "select * from employees limit 20"
#query="create database Employees"
#query= "create table persons(id int(50),doj Date,first char(50),last char(50),gender char(10),dob Date)"
query="insert into persons(id,doj,first,last,gender,dob) values (12,'2022-05-19','vishal','shahane','male','1994-06-11');"
#query="insert into persons(id,doj,first,last,gender,dob) values (11,'2021-08-19','vaibhav','jare','male','1999-06-11');"
cur.execute(query)
sel= "select * from persons;"
cur.execute(sel)

print('success')
for _id,_doj,_first,_last,_gender,_dob in cur:
    #print('id:',_id,'\nDOJ:',_doj,'\nDOB:',_dob,'\nFirst_Name:',_first,'\nLast_Name:',_last,'\nGender:',_gender)
    print(_id,_doj,_first,_last,_gender,_dob,sep="\n")
cur.close()
con.close()    