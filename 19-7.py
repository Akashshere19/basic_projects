
"""
#single class
class Vehicle: #create class
    def __init__(self, brand, model, type):
        self.brand = brand
        self.model = model
        self.type = type
        self.gas_tank_size = 14
        self.fuel_level = 0

    def fuel_up(self):  #create method
        self.fuel_level = self.gas_tank_size
        print('Gas tank is now full.')

    def drive(self):    #create method
        print(f'The {self.model} is now driving.')

    def update_fuel_level(self, new_level): #method fo checking level
        
        if new_level <= self.gas_tank_size:
            self.fuel_level = new_level
        else:
            print('Exceeded capacity')    

#create object
veh= Vehicle('Honda', 'Ridgeline', 'Truck')
print(veh.model)#call object
print(veh.type)
veh.fuel_up() #call method
#calling multiple object
veh2=Vehicle('Bajaj', 'Ridgeline', '4 weeler')
print(veh2.model)
print(veh2.type)
veh2.fuel_up()
veh2.update_fuel_level(16)# call for update attribute """

"""
class MyNewClass:
    '''This is a docstring. I have created a new class'''
    pass


my = MyNewClass()
print(MyNewClass)"""

'''
class Person:
    "This is a person class"
    

    def greet(self,grandfathername):
        self.grandfathername=grandfathername
        print("grandfatherName:",self.grandfathername)
        

    def Greet(self,fathername):
        self.fathername = fathername
        print("fatherName:",self.fathername)
    def Greet1(self,sonname):
        self.sonname = sonname
        print("SonName:",self.sonname)
    
print("Data for harry")        
harry=Person()
harry.greet("shankar")
harry.Greet('vilas')
harry.Greet1('pavan')

print("\nData for om")
om=Person()
om.greet("shamrao")
om.Greet('gajanan')
om.Greet1('om')


class Person:
    def fun(self,grandfather,father,son):
        self.grandfather=grandfather
        print(self.grandfather)
        self.father=father
        print(self.father)
        self.son=son
        print(self.son)

harry=Person()
harry.fun("sham","gajanan","pavan") '''

'''

l=[1,2,3]
if type(l) is  list:
    print(1+1+True) # output 3



l1=[2,5,8,6]
print(l1[::-2])'''


'''

def p(n=3):
    if (n==0 or n==1 or n--2):
        return 0
    if (n==3):
        return 1
    else:
        return p(n-1) +  p(n-2) + p(n-3)

c=p()
print(c)'''



def f1():
    i = 0
    s= 0
    while(i<100):
        s=s+i
        s=i+s
        i +=1
    print(s)    


c=f1()



















        



















    



































