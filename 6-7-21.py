"""
def add():
  	  
    a=int(input("enter a value"))
    b=int(input("enter a value"))
    c=a+b
    return c
print(add())"""

"""
def add(a,b):
    c=a+b
    return c
print(add(12,16))"""

"""
def my_function(fname):  
                        print(fname + " Refsnes" +  "\thello")
my_function("Emil")
my_function("Tobias")
my_function("Linus") """

"""
def my_function(*kids):
    for i in kids:
        print("The youngest child is",i)
    
my_function("Emil", "Tobias", "Linus")"""


'''
def my_function(**child):
    print("The youngest child is ",child['child1'])
my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linus")'''

"""
def fun():
    print("hello")
    fun()   #recursion 
fun()"""
'''
def add(a,b):
    c=a+b
    print(c)
print(add(12,12)) '''
'''
import heapq
numbers = [1, 4, 2, 100, 20, 50, 32, 200, 150, 8]
print(heapq.nlargest(9, numbers))
print(heapq.nsmallest(4,numbers))'''
'''
def many_types(x):
 if x < 5:
        while x <10:
            
            print("hello")
            x+=1
     
    #return "Hello!"
 else:
     return "please enter small no"
print(many_types(6))
print(many_types(4))'''
'''
def fun(*ar):
    print(ar)

fun([1,3,4])

x=0
while x <5:
    print("hi")
    x+=1 '''

'''
def myFun(x):
    x[0] = 20
    x[3] = 20
  
lst = [10, 11, 12, 13, 14, 15]
myFun(lst)
print(lst)'''
'''
def swap(x, y):
   
    x,y=y,x
    print("x=",x)
    print("y=",y)
# Driver code

swap(x=20,y=80)'''
'''
def func(**kwargs):
 
     for name, value in kwargs.items():
                     print(name, value)
func(value1='one', value2=2, value3=3)

my_dict = {'foo': 1, 'bar': 2}
func(**my_dict)'''
'''
def f1(**kwargs):
 print(len(kwargs))
f1(a=1, b=2,c=3)'''

'''
def f1(x):
    x=20
    return x
x=10
f1(x)
print(x)'''
'''
def fun(x,y=7):
    print("x=",x)
    print("y=",y)
    
fun(20)'''
'''
def myFun(**argv):
    for key,value in argv.items():
            print(key,value)
  
  
myFun(one='Hello', two='Welcome',three='to',four='GeeksforGeeks')'''
'''
def f1(L):
    
    
    print("".join(L))

f1(L = ['a','b','c','d'])'''
'''
y = 8
z = lambda x : x * y
print (z(6))'''
'''
def fun(**data):
    for key,value in data.items():
        
        print(key,value)

        
fun(one='1',two='2',java='c++',java1='c')'''
'''
def fun(*arg):
    sum=1
    for i in arg:
        sum1=i+sum
        
        print( sum1)

    
(fun(3,5,6,7,8,9,1))'''
'''
from time import sleep
def fun(**data):
    for key,value in data.items():
        print(key,value)
        sleep(1)
        
fun(name='janvi',age=20,mob=9766)
sleep(2)
print("sent to dehli")'''
'''
def multiply(x, y):
    print('multiply {} and {}'.format(x,y))
    result = x * y
    return result
    result =x / y
    return result
 

#if __name__ == '__main__':
answer = multiply(3,4)
print('Answer:', answer)
answer1 = multiply(3,8)
print('Answer:', answer1)
answer2 = multiply(9,4)
print('Answer:', answer2)
print('Answer is',multiply(3,7))'''
'''
#example for dic,list,string
d={'key':123,'key2':'value2','key3':{'4.8':'hello'}}
print(d['key2'],['key3'])
print(d['key3']['4.8'].upper())

s='django'
print(s[2])
print(s[1:4])
print(s[-1::-1])

l=[1,2,3,[3,5,'hello']]
print(l[3][2])
l[3][2]='goodbye'
print(l)'''
'''
#default arguments
def fun(x,y=6):
    print(x)
    print(y)
    
fun(2)
#keyword argument
def fun(x,y):
    print(x)
    print(y)
    
fun(x=2,y=28)'''

'''
class ABC :
	def method_abc (self):
		print("I am in method_abc of ABC class.")

class_ref = ABC() # object of ABC class
class_ref.method_abc()'''
'''
total = 0  #gloabal variable
def sum(arg1,arg2):
    total=arg1+arg2 #local variable
    print("this is local value ",total)
    return total
      
sum(12,13)
print('this is global value',total)'''
'''
sum=0
def f1(s1,s2):
    #global sum
    sum =s1-s2
   
    print('this is local value',sum)
    
f1(12,9)
print('this is global value',sum)'''

m=20
def f():
    m=m+1
    
print(m)
f()
print(m)
