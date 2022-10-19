"""
class A:
    num = 20
class B(A):
    pass
class C(A):
    pass
inst = C()
print(inst.num) """

"""
#heirachical Inheritance

class A:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class B(A):
    def __init__(self,name,age,no,adhar):
        A.__init__(self,name,age)
        self.no=no
        self.adhar=adhar

    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("no:",self.no)
        print("Adhar:",self.adhar)
        
class C(A):
    def __init__(self,name,age,address,voter):
        A.__init__(self,name,age)
        self.add=address
        self.vot=voter
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        
        
        print("Adress:",self.add)
        print("Voter_id",self.vot)

emp = C("akash",23,"abc",234)
emp.display()
print("\nDetails for class B")
emp1 = B("sham",26,"pune","ZP259FG")
emp1.display()"""

"""
#heirachical inheritance

class Student():  # parent class
   # constructor of parent class
   def __init__(self, name, enrollnumber):
      self.name = name
      self.enrollnumber = enrollnumber
   def display(self):
      print(self.name)
      print(self.enrollnumber)
# child class
class College( Student ):
   def __init__(self, name, enrollnumber, admnyear, branch):
      self.admnyear = admnyear
      self.branch = branch
      # invoking the __init__ of the parent class
      Student.__init__(self, name, enrollnumber)
# child class
class University( Student ):
   def __init__(self, name, enrollnumber, refno, branch):
      self.refno = refno
      self.branch = branch
      # invoking the __init__ of the parent class
      Student.__init__(self, name, enrollnumber)
# creation of an object for base/derived class
obj_1 = College('Rohit',42414802718,2018,"CSE")
obj_1.display()
obj_2 = University ('Rohit',42414802718,"st2018","CSE")
obj_2.display()
obj_3=Student('Vithal',4267545397)
obj_3.display()
obj_3.branch ="mechanical"
print(obj_3.branch)"""


"""
# Hierarchical inheritance
 
 
# Base class
class Parent:
      def func1(self):
          print("This function is in parent class.")
 
# Derived class1
class Child1(Parent):
      def func2(self):
          print("This function is in child 1.")
 
# Derivied class2
class Child2(Parent):
      def func3(self):
          print("This function is in child 2.")
  
# Driver's code
object1 = Child1()
object2 = Child2()
object1.func1()
object1.func2()
object2.func1()
object2.func3()  """

"""
class Student:
    def getStudentInfo(self):
        self.__rollno=input("Roll Number: ")
        self.__name=input("Name: ")

    def PutStudent(self):
        print("Roll Number : ", self.__rollno,"Name : ", self.__name)

class Bsc(Student):
    def GetBsc(self):
        self.getStudentInfo()
        self.__p=int(input("Physics Marks: "))
        self.__c = int(input("Chemistry Marks: "))
        self.__m = int(input("Maths Marks: "))

    def PutBsc(self):
         self.PutStudent()
         print("Marks is Subjects ", self.__p,self.__c,self.__m)

class Ba(Student):
    def GetBa(self):
        self.getStudentInfo()
        self.__h = int(input("History Marks: "))
        self.__g = int(input("Geography Marks: "))
        self.__e = int(input("Economic Marks: "))

    def PutBa(self):
         self.PutStudent()
         print("Marks is Subjects ", self.__h,self.__g,self.__e)

print("Enter Bsc Student's details")
student1=Bsc()
student1.GetBsc()
student1.PutBsc()

print("Enter Ba Student's details")
student2=Ba()
student2.GetBa()
student2.PutBa()"""

"""
# Parent class created
class Parent:
    parentname = ""
    childname = ""
 
    def show_parent(self):
        print(self.parentname)
 
 
# Son class inherits Parent class
class Son(Parent):
    def show_child(self):
        print(self.childname)
 
 
# Daughter class inherits Parent class
class Daughter(Parent):
    def show_child(self):
        print(self.childname)
 
 
s1 = Son()  # Object of Son class
s1.parentname = "Mark"
s1.childname = "John"
s1.show_parent()
s1.show_child()
 
d1 = Son()  # Object of Daughter class
d1.childname = "Riya"
d1.parentname = "Samule"
d1.show_parent()
d1.show_child()"""


