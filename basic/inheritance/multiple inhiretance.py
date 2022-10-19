
"""
#Multiple Inheritance
class A:
    str1 = "Hello "
class B:
    str2 = "World"
class C(A, B):
    def display(self):
        return self.str1 + self.str2
print(C().display()) """

"""
#Multiple Inhiretance
class length:
l = 0
def length(self):
return self.l
class breadth:
b = 0
def breadth(self):
return self.b
class rect_area(length, breadth):
def r_area(self):
print("The area of rectangle with length "+str(self.l)+" units and breadth "+
str(self.b)+" units is "+str(self.l * self.b)+" sq. units.")
o = rect_area()
o.l = int(input("Enter the required length for rectangle: "))
o.b = int(input("Enter the required breadth for rectangle: "))
o.r_area() """

"""
#Multiple Inhiretance
class A:
def A(self):
print('This is class A.')
class B:
def B(self):
print('This is class B.')
class C(A,B):
def C(self):
print('This is class C which inherits features of both classes A and B.')
o = C()
o.A()
o.B()
o.C() """
"""
#Multiple Inhertance
# Base class1
class Mother:
    mothername = ""
    def mother(self):
        print(self.mothername)
 
# Base class2
class Father:
    fathername = ""
    def father(self):
        print(self.fathername)
 
# Derived class
class Son(Mother, Father):
    def parents(self):
        print("Father :", self.fathername)
        print("Mother :", self.mothername)
 
# Driver's code
s1 = Son()
s1.fathername = "RAM"
s1.mothername = "SITA"
s1.parents()   """


"""
#Multiple Inhertance
# Father class created
class Father:
    fathername = ""
 
    def show_father(self):
        print(self.fathername)
 
 
# Mother class created
class Mother:
    mothername = ""
 
    def show_mother(self):
        print(self.mothername)
 
 
# Son class inherits Father and Mother classes
class Son(Father, Mother):
    def show_parent(self):
        print("Father :", self.fathername)
        print("Mother :", self.mothername)
 
 
s1 = Son()  # Object of Son class
s1.fathername = "Mark"
s1.mothername = "Sonia"
s1.show_parent()"""

"""" #Multiple inheritance       
class father:
      
      def show_father(self):
          print(self.fathername)      
class son:
      
      def show_son(self):
          print(self.sonname)

class mother:
    def show_mother(self):
        print(self.mothername)
class sister(father,son,mother):
    def show_sister(self):
        print(self.sistername)        

fam = sister()
fam.sonname="akash"
fam.mothername="jyoti"
fam.fathername="...."
fam.sistername="...."
fam.show_son()
fam.show_mother()
fam.show_father()
fam.show_sister()"""



