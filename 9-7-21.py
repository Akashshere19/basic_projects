'''
def recursive_factorial(n):  
   if n == 1:  
       return n  
   else:  
       return n * recursive_factorial(n-1)

print(recursive_factorial(5)) '''
'''
def printFun(test):
 
    if (test < 1):
        return 
    else:
 
        print(test, end=" ")
        printFun(test-1)  # statement 2
        print(test, end=" ")
        return
 
# Driver Code
test = 3
printFun(test)'''

'''
def my_function():
  print("Hello from a function")

my_function()


def evenOdd(x):
    if (x % 2 == 0):
        print ("even")
    else:
        print ("odd")
  
# Driver code to call the function
evenOdd(2)
evenOdd(3)'''

'''
def say_Hi():
    "Hello! geeks!"
 
 
print(say_Hi.__doc__)'''

'''
def swap(x, y):
    #print(x,y)
    temp = x
    x = y
    y = temp
    print('x:',x,'y:',y) 

# Driver code
x = 2
y = 3
swap(3,2)
print(x)
print(y)'''

'''
def myFun(x, y=50):
    print("x: ", x)
    print("y: ", y)

myFun(10) '''




"""
def myFun(*argv):
	for arg in argv:
		print(arg)


myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')"""

"""
def myFun(**kwargs):
    for key, value in kwargs.items():
        print("%s == %s" % (key, value))
 
 
# Driver code
myFun(first='Geeks', mid='for', last='Geeks')"""

"""
def myFun(arg1, *argv):
	print ("First argument :", arg1)
	for arg in argv:
		print("Next argument through *argv :", arg)

myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')"""

"""
def myFun(arg1, arg2, arg3):
	print("arg1:", arg1)
	print("arg2:", arg2)
	print("arg3:", arg3)
	
args = ("Geeks", "for", "Geeks")
myFun(*args)

kwargs = {"arg1" : "Geeks", "arg2" : "for", "arg3" : "Geeks"}
myFun(**kwargs)"""

"""
def sq(a):
    return a*a
res=sq(5)
print(res)"""

"""
def is_even(n):
    return n%2==0

nums=[1,8,2,5,6,7,9]
evens=list(filter(lambda n:n%2==0,nums))

print(evens)"""

"""
def changeme( mylist ):
     print ("Values inside the function before change: ", mylist)
     mylist[2]=50
     print ("Values inside the function after change: ", mylist)
     return

mylist = [10,20,30]
changeme( mylist )
print ("Values outside the function: ", mylist)"""

"""
def changeme( mylist ):
     "This changes a passed list into this function"
     mylist = [1,2,3,4] 
     print ("Values inside the function: ", mylist)
     return

mylist = [10,20,30]
changeme( mylist )
print ("Values outside the function: ", mylist)
"""

"""
def printme( str ):
     "This prints a passed string into this function"
     print (str)
     return

printme( str = "My string")"""


'''
def printinfo( name,sex,mob,age = 35 ):
     
     print ("Name: ", name,'sex=',sex)

     print ("Age: ", age,'mob=',mob)
     return

printinfo( age=50,sex='male', name="miki",mob=9766)
printinfo( name="miki",sex='female',mob=9766 )

def f1(**tup):
    for key,value  in tup.items():
        print(key,value)
f1(name='akash',age=27,sex='male',mob=9766)'''


'''
def printinfo( arg1, *vartuple,**vardict ):
 
     print ("Output is: ")
     print (arg1)
     for var in vartuple:
         print (var)
     for key,value in vardict.items():
          
          print(key,value)

printinfo( 10 )
printinfo( 70, 60, 50 )

printinfo( 12,one='70', two='60', three='50' )'''










