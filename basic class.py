
class Employee: #create class
    name = "John"  #atrribute of class
    age = 26
    lname='bush'
    
 
 
e = Employee()  # create object of class
print(e.name, e.age)

"""
class Employee: #create class 
    def __init__(self, name, age): #init function method 
        self.name = name #instance object or attribute
        self.age = age    #instance object
 
 
e = Employee("Sam", 36) # class object
print(e.name, e.age) 

e1= Employee("ram", 26) # class  2nd object
print(e1.name, e1.age)"""
"""
class Employee:
    def __init__(self, name, age):
        self.name = name
        self.age = age
 
    def details(self):  #method 
        print("Employee Name:",  self.name)
        print("Employee Age:", self.age)
 
 
emp = Employee("Sam", 36)
emp.details() #access method through object

del emp.name #delete name """

"""
class student: #create class
    def __init__(self,age,mob):
        self.Name="Akash" #create atrribute 
        self.Age=age
        self.Mob=mob
    def show(self):
        print(self.Name,self.Age,self.Mob)



emp= student(24,9766) #class 1st object
emp.show()
emp2=student(23,9766646) #class 2nd object

emp2.show()"""







