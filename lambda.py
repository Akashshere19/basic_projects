'''def sq(a):
    for i in a:
        s=i**2
        
        print(s)
        

a=[1,2,4,8]        
sq(a)'''

'''
b=[1,2,4,8]
def sq(x):
    return x*x                                                                                                                                             
print(list(map(sq,b)))'''

'''
c=[1,2,4,8]
print(list(map(lambda x:x*x,c)))'''


'''
my_list = [12, 65, 54, 39, 102, 339, 221, 50, 70, ]
for i in my_list:
    if i % 13 == 0:
        print(i)
else:
    print("it is not divisible")
print(i)

result = list(filter(lambda x: (x % 13 == 0), my_list))
print(result) '''

'''
x = lambda a : a + 10
print(x(5))'''
'''
x=lambda a,b:a*b
print(x(2,4))

a=2
b=4
print(a*b)'''
'''
x=lambda a,b:a if a>b else b
print(x(3,5))'''

'''
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))

def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)
mytripler = myfunc(3)

print(mydoubler(11))
print(mytripler(11))'''
'''
sequences = [10,2,8,7,5,4,3,11,0, 1]
filtered_result = filter (lambda x: x > 4, sequences) 
print(list(filtered_result))'''
''''
sequences = [10,2,8,7,5,4,3,11,0, 1]
filtered_result = map (lambda x: x*x, sequences) 
print(list(filtered_result))'''
'''
def sq(n):
    x=n**2
    return x

print(sq(2))

x=lambda n:n**2 
print(x(4,5))'''
'''
x=lambda n:n*(n+5)
    
print(x(2))'''
'''
x=lambda x,y:("x is greater than y") if x > y else ("y is greater than x")

print(x(5,6))
print(x(20,8))'''
'''
y=lambda x:( x%2==0 and 'even'or'odd')
print(y(3))

y=lambda x:('even' if x%2==0 else 'odd')
print(y(4))'''

'''print((lambda x, y, z=3: x + y + z)(1, y=2))
print((lambda *arg:sum(arg))(1,2,3,4,5,6))
print((lambda **arg:sum(arg.values()))(one=1,two=2,three=3))
print(( lambda s: s.upper())('hey hello how are you...?'))

greeting = lambda x, *args, **kwargs: print(x, args, kwargs)
greeting('hello', 'world', world='world')


my_list = [3, -4, -2, 5, 1, 7]
s=sorted( my_list, key=lambda x: abs(x))

print(s)'''

n1=[1,2,3]
n2=[4,5,6]
n3=[7,8,9]
print(n1)
print(n2)
print(n3)
result=map(lambda x,y,z:x+y+z,n1,n2,n3)
print(list(result))
