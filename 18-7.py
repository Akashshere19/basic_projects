'''class student:
    
    def hello(self):
        self.name="akash"
        self.age=10
        print(self.age)
        print(self.name)
std=student()
(std.hello())
#print(std.name())'''
'''
def decor1(func):
	def inner():
		x = func()
		return x * x
	return inner

def decor(func):
	def inner():
		x = func()
		return 2 * x
	return inner

@decor1
@decor
def num():
	return 10

print(num())'''

'''
def shout(text): 
    return text.upper() 
  
def whisper(text): 
    return text.lower() 
  
def greet(func): 
    # storing the function in a variable 
    greeting = func("""Hi, I am created by a function passed as an argument.""") 
    print (greeting) 
  
greet(shout) 
greet(whisper) '''
'''
def func():  
     print("We are in first function")  
     def func1():  
           print("This is first child function")  
     def func2():  
           print("This is second child function")  
     func1()  
     func2()

func()'''
'''
def add(x):  
    return x+1  
def sub(x):  
    return x-1  
def operator(func, x):  
    temp = func(x)  
    return temp  
print(operator(sub,10))  
print(operator(add,20)) '''
'''
def hello():  
    def hi():  
        print("Hello")  
    return hi  
new = hello()  
new() '''
'''
class Student:  
    def __init__(self,name,grade):  
         self.name = name  
         self.grade = grade  
    @property  
    def display(self):  
         return self.name + " got grade " + self.grade  
  
stu = Student("John","B")  
print("Name:", stu.name)  
print("Grade:", stu.grade)  
print(stu.display)'''

'''
a=10 #global variable
def f1(name):
    print(name)
    global a #access local variable
    a=20 #local variable
(f1('Akshata'))
print(a)'''
'''
def function1():
    print("hello")
    
func2=function1
del function1
func2() #print hello becoz function1 is already came in func2'''
'''
#example of decorator
def f1(name):
    print("outside function")
    def f2():
        print("inside function")
        name()
        print("hi")
    return f2
@f1       
def f3():
    print("its function 3")

#f3=f1(f3)
f3()'''
'''
#example for only inner execute
def outer():
    message="1st function"
    def inner():
        outer()
        print("inside function")
    return inner  
  
my=outer()
my()'''


#example for only both
def outer(msg):
    print("outer")
    def inner():
        print("its inner")
        return msg
    return inner()

def display():
    print("it's 3rd function")

display1=outer(display)
display1()

'''
#example for only both
def outer(msg):
    
    def inner():
        print("its inner")
        return msg
    return inner()
@outer
def display():
    print("it's 3rd function")

#display1=outer(display)
display()'''
def f1(msg):
    print("hi")
@f1    
def f2(h):
    print("hiii")
    

obj=f2(12)

obj()













    

