'''
class Student():   # parent class

   # constructor of parent class
   def __init__(self, name, enrollnumber):
      self.name = name
      self.enrollnumber = enrollnumber
   

class College( Student ):  # child class
   def __init__(self, name, enrollnumber, admnyear,passyear, branch):
      self.admnyear = admnyear
      self.branch = branch
      self.passyear=passyear
      # invoking the __init__ of the parent class
      Student.__init__(self, name, enrollnumber)
   def display(self):
      print(self.name)
      print(self.enrollnumber)
      print(self.admnyear)
      print(self.passyear)
      
# creation of an object for base/derived class
obj = College('Rohit',42414802718,2018,2021,"CSE")
obj.display()
print(obj.branch)

obj2 = College("Akshay",25,2019,2022,"Entc")
obj.display()
print(obj.name)'''

"""
#Single Inheritance
# Parent class created
class Parent:
    #parentname = ""
    #childname = ""
 
    def show_parent(self):
        print(self.parentname)
 
 
# Child class created inherits Parent class
class Child(Parent):
    def show_child(self):
        print(self.childname)
 
 
ch1 = Child()  # Object of Child class
ch1.parentname = "Mark"   # Access Parent class attributes
ch1.childname = "John"
ch1.show_parent()   # Access Parent class method
ch1.show_child()    # Access Child class method  """




"""
#Single inheritance
#Base class
class Parent_class(object):
# Constructor
def __init__(self, value1,value2):
self.value1 = value1
self.value2 = value2
# To perform addition
def Addition(self) :
print(" Addition value1 : " , self.value1)
print(" Addition value2 : " , self.value2)
return self.value1 + self.value2
def multiplication(self) :
print(" multiplication value1 : " , self.value1)
print(" multiplication value2 : " , self.value2)
return self.value1 * self.value2
def subraction(self) :
print(" subraction value1 : " , self.value1)
print(" subraction value2 : " , self.value2)
return self.value1 - self.value2
# derived class or the sub class
class Child_class(Parent_class):
pass
# Driver code
Object1 = Child_class(10,15)  # parent class object
print(" Added value :" , Object1.Addition() )
print( " " )
Object2 = Child_class(20,30)  # parent class object
print(" Multiplied value :" , Object2.multiplication() )
print( " " )
Object3 = Child_class(50,30)  # parent class object
print("Subracted value :" , Object3.subraction() ) """



"""
#single Inheritance
class Family:
    # Parent class constructor
    def __init__(self, name):
        self.name = name
 
 
# Father class inherited from Family
class Father(Family):
    # Child class constructor
    def __init__(self, name, age):
        #  Parent class constructor called from child class
        Family.__init__(self, name)
        self.age = age
 
 
f = Father("Mark", 36)
print(f.name)
print(f.age)"""

"""
#single Inhirtance
class Family:
    def show_family(self):
        print("This is our family:")
 
 
# Father class inherited from Family
class Father(Family):
    fathername = ""
 
    def show_father(self):
        print(self.fathername)
 
 
# Mother class inherited from Family
class Mother(Family):
    mothername = ""
 
    def show_mother(self):
        print(self.mothername)
 
 
# Son class inherited from Father and Mother classes
class Son(Father, Mother):
    def show_parent(self):
        print("Father :", self.fathername)
        print("Mother :", self.mothername)
 
 
s1 = Son()  # Object of Son class
s1.fathername = "Mark"
s1.mothername = "Sonia"
s1.show_family()
s1.show_parent()"""



"""
#single Inheritance

class Person(object):
       
    # Constructor
    def __init__(self, name):
        self.name = name
   
    # To get name
    def getName(self):
        return self.name
   
    # To check if this person is an employee
    def isEmployee(self):
        return False

class Employee(Person):
   
    # Here we return true
    def isEmployee(self):
        return True

emp=Person("akash")
print(emp.name)

print(emp.isEmployee())#show employee or not

emp2=Person("akshay")
print(emp2.name)

print(emp2.isEmployee())#show employee or not """

"""        
#single Inheritance

# parent class
class Person( object ):	

		# __init__ is known as the constructor		
		def __init__(self, name, idnumber):
				self.name = name
				self.idnumber = idnumber
		def display(self):
				print(self.name)
				print(self.idnumber)

# child class
class Employee( Person ):		
		def __init__(self, name, idnumber, salary, post):
				self.salary = salary
				self.post = post

				# invoking the __init__ of the parent class
				Person.__init__(self, name, idnumber)

				
# creation of an object variable or an instance
a = Employee('Rahul', 886012, 200000, "Intern")	

# calling a function of the class Person using its instance
a.display()  """





        
