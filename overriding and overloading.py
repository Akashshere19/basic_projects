'''
#Example of method overloading
class methodOverloading:                          
    def display(self,a):
        print("method invoked from base class",a)


    def display(self,a,b):
        
        print("method invoked from derived class",b,a)
        
obj=methodOverloading()
obj.display(12,23)''' 

#Example of avaiding method overriding
class methodOverride1:                          
    def display(self):
        print("method invoked from base class")

class methodOverride2(methodOverride1):
    def display(self):
        
        print("method invoked from derived class")

ob=methodOverride2()
ob.display()

#Example of avaiding method overriding
class methodOverride1:                          
    def display(self):
        print("method invoked from base class")

class methodOverride2(methodOverride1):
    def display(self):
        super().display()
        print("method invoked from derived class")

ob=methodOverride2()
ob.display()

"""
#Example of overloading
class OverloadDemo:
   def multiply(self,a=None,b=None,c=None):
       if a!= None and b!= None and c != None:
                     s=a*b*c
                     
       elif a!=None and b!=None:
                     s=a*b
                     
       else:
           s=a
       return s
   '''def multiply(self,a, b, c):
       print(a*b*c)'''
m=OverloadDemo()
print(m.multiply(2,5))"""

"""
#Example of overloading
class Person:
    def Hello(self, name=None):
        if name is not None:
            print('Hello ' + name)
        else:
            print('Hello ')
   
        
        
obj = Person()
# Call the method
obj.Hello()
# Call the method with a parameter
obj.Hello('Edureka') """

'''
#example of overloading
class func:
    def f1(self,a=13):
        self.name = a
        print(a)
        
    def f1(self,a,b):
        
        
        self.age = b
        print(a,b)
        
cl_ob=func()
cl_ob.f1(11,12) '''

'''
#example of overriding
class cal:
    def f1(self,a=122):
        self.name=a
        print(a)
        
class csl(cal):
    def f1(self,b):
        self.age=b
        
        super().f1() # using this command we print value of a
        print(b)
        
c=csl()
c.f1(12) '''
'''
#example of overriding       
class akash:
    def name(self,n='hello'):
        
        self.nem = n
        print(n)
    
    def srname(self,s='sham'):
        self.srnem = s
        
        print(s)
        
class amol(akash):
    def name(self,a):
        self.ns = a
        super().srname()
        super().name()
        print(a)


ob=amol()
ob.name('hi') '''


'''
def product(a,b):
    p=a*b
    print(p)
def product(a,b.c):
    p=a*b*c
    print(p)

product(3,9,2) '''

def add(data,*arg):
    if data=='int':
        ans=0
    if data=='str':
        ans=''
    for x in arg:
        ans=ans+x

    print(ans)
add('int',5,9,8,7,3)
add('str','dhj','gd')




































































