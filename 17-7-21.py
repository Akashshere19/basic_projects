'''
def x(val):
    print(val)
    val[0]=43
    val.append([23])
    val.extend([1,2,3])
    
val=[2,8,5]
x(val)
print("it's new:",val)
print(type(val))'''

'''
#function
def con():
    print("i5,16gb,1Tb")
    

con()
#class
class config:
    def con(self):
        print("i5,16gb,1Tb")
    def con1(self):
        print("it")
    
a='9'
com1 =config()
com1.con()
com1.con1()'''

'''       
class Person: #class create
  def __init__(self, name, age): #constructor
    self.name = name #instance obj
    self.age = age

p1 = Person("John",36) #class obj

print(p1.name) #access instance obj
print(p1.age)'''


'''class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age

   
  def myfunc(self):
    print("Hello my name is " + self.name)

p1 = Person("John", 36)
p1.myfunc()'''

"""
class Person:
  def __init__(self):
        self.name = "rohan"
        self.age = 27


p1=Person()
p1.name="shashi"
print(p1.name)
print(p1.age)
print(p1.name)"""

"""
# A Sample class with init method
class Person:

	# init method or constructor
	def __init__(self):
		self.name = 'akash'

	# Sample Method
	def say_hi(self):
		print('Hello, my name is', self.name)

p = Person()

print(p.name)
p.say_hi()"""

"""
class Dog:
	
	# A simple class
	# attribute
	attr1 = "mammal"
	attr2 = "dog"

	# A sample method
	def fun(self):
		print("I'm a", self.attr1)
		print("I'm a", self.attr2)

# Driver code
# Object instantiation
Rodger = Dog()

# Accessing class attributes
# and method through objects
print(Rodger.attr1)
Rodger.fun()"""

