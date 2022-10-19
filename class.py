'''
class Dog: 

	def fun(self):
		print("I'm a", self.attr1)
		print("I'm a", self.attr2)

Rodger = Dog()
print(Rodger.attr1)
Rodger.fun()'''

'''
class student:
    sn='xyz school'
std = student()
print(std.sn)'''


class student:
    pass
std=student()
print(type(std))

"""
class Student:
    count = 0
    def __init__(self):
        Student.count += 1


std=Student()
print(Student.count)
std1=Student()
print(Student.count)
std2=Student()
print(Student.count)"""

"""
class account:
    def __init__(self,a,b):
        self.accno=b
        self.accbal=b
     def f1(self,x,y):
        self.accno=x
        self.accbal=y    
   
        
acc1=account(12,88)
acc1.accno=11
acc1.accbal=500
print(acc1.__dict__)"""
'''
class Vehicle: #class create
    def __init__(self, model, type): #init function and its atrribute
        self.brand = 'bmw'
        self.model = model
        self.type = type
        self.gas_tank_size = 14
        self.fuel_level = 0

    def fuel_up(self): 
        self.fuel_level = self.gas_tank_size
        print('Gas tank is now full.')

    def drive(self):
        print(f'The {self.model} is now driving.')
veh= Vehicle('bh4','2 wheeler')
print(veh.brand)
veh.drive()
veh.fuel_up()

veh2= Vehicle('bh44','4 wheeler')
print(veh2.brand)
veh2.model()
veh2.fuel_up() '''






'''
def f1():
    global b
    b=5
    
b=9
f1()'''
'''
b=3
def f1():
    b=8
    print(b)
   
    print(globals()['b'])
f1()  '''

'''
# Python program to illustrate property() function
class Person:
    def __init__(self, name):
        self._name = name

    # getter function
    def get_name(self):
        print('Getting name...')
        return self._name

    # setter function
    def set_name(self, value):
        print('Setting name to:', value)
        self._name = value

    # deleter function
    def del_name(self):
        print('Deleting name...')
        del self._name

    # Set property() to use get_name, set_name and del_name methods
    name = property(get_name, set_name, del_name)

p = Person('David')
print(p.name)
p.name = 'Rocky'
del p.name'''






















