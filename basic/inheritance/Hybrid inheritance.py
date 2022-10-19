
"""
#Hybrid Inhiretance

# Python program to demonstrate
# hybrid inheritance


class School:
	def func1(self):
		print("This function is in school.")

class Student1(School):
	def func2(self):
		print("This function is in student 1. ")

class Student2(School):
	def func3(self):
		print("This function is in student 2.")

class Student3(Student1, School):
	def func4(self):
		print("This function is in student 3.")

# Driver's code
object = Student3()
object.func1()
object.func2()"""

"""
#Hybrid Inhiretance
class X:
    num = 10
class A(X):
    pass
class B(A):
    pass
class C(A):
    pass
class D(B, C):
    pass

ob = D()
print(D.num) """



