'''i=0
while i<5:
    print("hi")
    
    i+=1
i=0
while i<5:
    print("hi")
    if i==3:
        print("odd no",i)
    
    i+=1 
a=[1,2,3,4,5]
while a:
    print(a.pop())
count = 0
while (count < 5): count += 1; print("Hello Geek")

a=0
s="greekforce"
while a< len(s):
    print(a)
    if s[a]=='e' or s[a]=='r':
        a+=1
        continue
    print(s[a])
    a+=1
i=0
s="helloworld"
while i <len(s):
    i+=1
    pass
print(i)
    #i+=1
i=0
while i<4:
    i+=1
    print(i)
else:
    print("no break")
    
i=0
while i< 4:
    i+=1
    print(i)
    break
else:
    print("break")
i=0
while i<10:
    print('hi=',i)
    i+=1
    
else:
    print("break")
i=0
while i<10:
    print("i=",i)
    if i==2 or i==6 or i==8:
        print("continue")
        i+=1
        continue
    print(i)
    i+=1   

s = ['a','b','c','e','j','i','s','p','o','e']
e=0
other=0
while e < len(s):
    
    
    if s[e] == 'a' or s[e]=='e'or s[e]=='i'or s[e]=='o'or s[e]== 'u':
        vowels=s[e]
        e+=1
        print('vowel=',vowels)   
    else:
        other=s[e]
        e+=1 

    print('other=',other)  

tuple1 = ('a', 'e', 'i', 'o', 'u')

index = 0

while index<len(tuple1):
    
    print(tuple1[index],end=" ")
    
    index = index+1  

tup=(1,5,6,7,8,2,2,3,4,9)
a=0
sum=0
while a<len(tup):
    
    print(tup[a])
    sum =sum+tup[a]
    a+=1
print("total sum is",sum)

t=(1,1,1,8,9,4,2,8,6)
i=0
s=0
while i < len(t):
    
        s=s+t[i]
        i+=1
print(s)
i=0
while i < 10:
    i+=1
    if i==3:
        break
    print(i)
print("end loop")    

a=['foo','fhoor','bar','gar','jar']

s='car'
i=0  
while i<len(a):
    if a[i]==s:
       break
    i+=1
else:
    print(s,"not found")
a=['a','b','c']
while True:
    if not a:
        break
    print(a.pop())
d={1:'one',2:'two',3:'three'}
while len(d)>2:
    print(d.popitem())
print('Done.')   
a=['a','b','c','d','e','f']
while len(a)>3:
    print(a.pop())    
print('done')

a=['a','b','c','d','e','f']
while a:
    if len(a)<1:
        continue
    print(a.pop())
    
print('done.')

s = ""

n = 5
while n > 0:
    n -= 1
    if (n % 2) == 0:
        continue

    a = ['foo', 'bar', 'baz']
    while a:
        s += str(n) + a.pop(0)
        if len(a) < 2:
            break  
a=['a','b','c','d']
while a:
    print(a.pop())

a={1:'a',2:'b',3:'c'}
b={4:'x',5:'y',6:'z'}
i=7
while len(b)<i:
    c={**a,**b}
    i-=1
print(c)

a={1:'a',2:'b',3:'c'}
b={4:'x',5:'y',6:'z'}
i=7
if len(b)<i:
    c={**a,**b}
    i-=1
print(c)

mylist = ["apple", "banana", "cherry"]
i=0
while i<len(mylist):
    u=(mylist.pop())
    print(u)

    
list=["apple", "banana", "cherry", "apple", "cherry"]
for i in list:
    print(i)
l=[]
while len(l)<5:
    for i in range(0,5):
        l.append(i)
    print(l)
    if l[i]==4:
        t=l.remove(4)
        print('new',t)'''



'''

l=[1,7,3,4]
l.append([2,9,7,5,3])
l.extend([8,6,11,10])
l.insert(3,23)
l.remove(23)
l.pop()
print(l.count(3))
print(l)

s={2,4,2,9,6}
s.add((3,2,3,47,5))
s.update([21])
s1=s.union({33,31,34})
s.remove(9)
s.pop()
print(s)
#print(s1) '''
'''
#print * patterns
n=10
for i in range(1,n+2,1):
    for j in range(1,i+1):
        print('*',end = ' ')
    print('') # '''
'''
i=0
num =10
n=0
while i<=num:
    n=n+i
    i+=1
print(n)

s=0
n=10
for i in range(1,n+1,1):
    s+=i
print('\n')
print(s) 

n=10
s=sum(range(1,n+1))
print(s)
'''
'''#table of 2
for i in range(1,11,1):
    print(i*2)
    
'''

'''
row =5
col=5
for i in range(0,row+1):
    for j in range(col-i,0,-1):
        print(j,end =' ')
    print() '''
'''

for i in range(10):
    print('|') '''
'''    
i=0
while i< 10:
    print(i)
    i+=1 '''





'''  
    
class Student:
	id = None
	name = None
	
	def __init__(self, id, name):
		self.id = id
		self.name = name
	
	def print_values(self):
		print("ID: {}, NAME: {}".format(self.id, self.name))

s1 = Student(1, "Gaurav")

s2 = s1  
s2.name = "Akash"
s1.print_values()
s2.print_values()

list = [10, 80, 5, 60, 20, 40]
list[4]=34
print(list)'''
'''
lst= [
	{
		"id": 5,
		"name": "Gaurav"
	},
	{
		"id": 2,
		"name": "Akash"
	},
	{
		"id": 3,
		"name": "Nitin"
	},
	{
		"id": 50,
		"name": "Arun"
	},
	{
		"id": 25,
		"name": "Vishal"
	},
]

d='id'     
re = sorted(lst,key =lambda sub: sub[d])
print(re) '''
    
    

'''

class A:
	def my_method(self, text):
		print("In class A: {}".format(text))

class B(A):
	def my_method(self, text):
		print("In class B: {}".format(text))

class C(A):
	def my_method(self, text):
		print("In class C: {}".format(text))

class D(B, C):
	def execute(self):
		self.my_method("Smart Monitor")

d = D()
d.execute() '''


lst= [
	{
		"id": 5,
		"name": "Gaurav"
	},
	{
		"id": 2,
		"name": "Akash"
	},
	{
		"id": 3,
		"name": "Nitin"
	},
	{
		"id": 50,
		"name": "Arun"
	},
	{
		"id": 25,
		"name": "Vishal"
	},
]
         
k= 'id'

result = sorted(lst,key = lambda s:s[k])
print(result)


    
list=[{'name': 'Abdullah', 'age': 22},
 {'name': 'Citrus', 'age': 33},
 {'name': 'Ben', 'age': 44}, 
 {'name': 'Dough', 'age': 55}]



result = sorted(list,key =lambda x:x['age'])
print(result)









    
