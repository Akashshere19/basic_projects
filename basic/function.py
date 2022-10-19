
'''
def f1(a,b):
    print(a+b)
f1()    

def f1(a=12,b=13):
    print(a+b)
f1()

def f1(a=12,b=13):
    print(a+b)
f1()    



def f1(a=12,b=13):
    return(a+b)
n=f1()    

print(n) '''




'''
def fun():
    print("hello")
fun()'''

'''
def fun(name="hi"):
    return("Hi "+name)
fun()
a=fun()
b=fun()
print(fun(),a,b)'''

'''
def fun(name):
    print("Hello",name)
fun("World") '''
'''
def fun(name):
    return ("Hi"+name)

obj=(fun("Akash"))
print(obj)'''
'''
def fun(a=2,b=3,c=5,d=9):
    e=a+b+c+d
    return e
ob=fun()
print(ob)'''
'''
def fun(*a):
    e=sum(a)
    return e

    
obj=fun(2,3,5,9)
print(obj)'''

'''
def my_function(**kid):
        print("His  name is "+kid["fname"] + kid["lname"])
        print(kid.values())

my_function(fname = "tukaram", lname  = "gaikwad")'''

'''
def printinfo( arg1, *vartuple,**agr ):
      "This prints a variable passed arguments"
      print ("Output is: ",arg1)
      #print(arg1)
      #for var in vartuple:
      print(vartuple)
      print(agr)
      
      #return

# Now you can call printinfo function
printinfo( 10 )
printinfo( 70, 60, 50 )
printinfo(a=2,b=9,c=8)'''
'''
def addNum(num1,num2):
    if type(num1)==type(num2)==type(12):
        return num1+num2
    else:
        return "sorry"
result=addNum(2,6)
print(result)

result1=addNum('2',2)
print(result1)'''

'''
my_list=[1,2,3,4,5,6,7,8,9]

eve=filter(lambda num: print (list(eve)) num%2==0,my_list)'''
'''
num=[1,2,4,3,3]
num1=[1,2,3,3]
def array(num):
    for i in range(len(num)):
        if num[i]==1 and num[i+1]==2 and num[i+2]==3:
            return True
    return False    
result=array(num)
print(result)

result1=array(num1)
print(result1)'''
'''
strn='hello'
def str(strn):
    
   # print(len(strn))
       #if strn[0]=='h' and strn[2]=='l' and strn[4]=='o':
            return strn[0:5:2] 
            
result=str(strn)
print(result)
'''
'''
s='hellohellohello'
print(len(s))
print(s[::2])'''
'''
c=2
b=5
def fun(n):
    global c
    print("global value",c)
    n=c+b #addition for global c
    print(n)
    c=4
    print("local value",c)
     
    n= c + b #addition for lacal c
    print(n)
fun(n=0)

def fun(cname,name="hi"):
    
    print(name,cname)
    return("Hi "+name,cname)
fun("akash")
#fun()
print(fun("aka"))
    

def addNum(num1,num2):
    if type(num1)==type(num2)==type(12):
        return num1+num2
    else:
        return "sorry"
result=addNum(2,6)
print(result)

result1=addNum(8,2)
print(result1)

def addNum(*n):
    for i in n:
        if type(i) == type(12):
            print(i)
        elif type(i)!= type(12):
            
                print("this not int type",i)
        
rs=addNum(12,13,11,'st','shree')

def f(l):
    l1=[2,9,6,4,3]
    l2=l+l
    print(l)
    print(l2)
    print(type(l))
    for i in l2:
        if type(i) == tuple:
            print(i,"this is tuple item")
            for j in i:
                print(j)
        else:
            print(i,'this is list item')
    
f([12,16,19,(12,19)])

def f1(l):
    for i in l:
        l1=[]
        if i % 2==0:
            l1.append(i)
        
        else:
 
            print('this item is odd',i)
        print(l1)
        
f1([1.9,2,4,8,3,0,1,6,12])

def f1(*n):
    print(n,type(n))
    s=set(n)
    
    print(s,type(n))
f1(1,2,9)  

def f1(**k):
    print(k)
f1(a='ap')
f1(fruit='ban',veg='ca')

def main():
     print ("Hello World!")
print ("Guru99")
main()'''
'''
def f2(**a):
    print(a)
    
def f1(*a):
    print(a)
obj=f1(2,9,3)    
print(obj)
f2(a='a',h='')'''
'''
a=1
def f():
    b=8
    def f1():
        c=4
        print(locals().keys())
        #print('b' in locals())
        #print('b' in globals())
    f1()       
print(f()) '''    
'''
def br():
    for i in range(10):
        if i % 2==0:
            #return i
             print(i)
        
        return i
print(br())'''
'''
x=map(lambda e:e.upper(),('a','b','c'))
print(tuple(x))'''

'''
x=lambda s:s.strip().upper()
print(x('hello \t' 'world'))'''
'''
def f(x):
    x[0]=9
    print(x)
y=[7,9,8]
f(y)#here in x assign y  '''
'''
def f(x):
    def inc(y):
        nonlocal x
        x+=y
        return x
    return inc
incone=f(2)
incone(8)'''

'''
lambda_factorial = lambda i:1 if i==0 else i*lambda_factorial(i-1)
print(lambda_factorial(4))

s=lambda x:x*x
print(s(4))'''

'''
t= filter(lambda a,x:a+x,[2,9,7])
print(t) '''

'''
def f1(n=input("enter name :")):
    return ("Hi"+n)
def f2(m=input("enter name :")):
    return ("hello"+ m)
def f3(k=input("enter name :")):
    return ("hello"+ k)
def f4(p=input("enter name :")):
    return ("hello"+ p)
f1()
b=f1()
c=f2()
d=f3()
a=f4()
print(f1(),a,b,"\n",c,"\n",d)'''


