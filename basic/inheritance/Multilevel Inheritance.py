'''
# multilevel inheritance

# Base class
class Grandfather:

	def __init__(self, grandfathername):
		self.grandfathername = grandfathername

# Intermediate class
class Father(Grandfather):
	def __init__(self, fathername, grandfathername):
		self.fathername = fathername

		# invoking constructor of Grandfather class
		Grandfather.__init__(self, grandfathername)

# Derived class
class Son(Father):
	def __init__(self,sonname, fathername, grandfathername):
		self.sonname = sonname

		# invoking constructor of Father class
		Father.__init__(self, fathername, grandfathername)

	def print_name(self):
		print('\nGrandfather name :', self.grandfathername)
		print("Father name :", self.fathername)
		print("Son name :", self.sonname)

# Driver code
s1 = Son('Prince', 'Rampal', 'Lal mani')
#print(s1.grandfathername)
s1.print_name()
s2= Son('pappu','pan','masala')
s2.print_name()'''

"""
#Multilevel Inheritance
class Parent:
    str1 = "Python"
class Child(Parent):
    str2 = "Geeks"
class GrandChild(Child):
    def get_str(self):
        print(self.str1 + self.str2)
person = GrandChild()
person.get_str() """


