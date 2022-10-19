''''a=iter('Hello')
print(a)#for type
print(next(a))
print(next(a))
print(next(a))
print(next(a))'''

'''
strg="Akash"
it = iter(strg)
print(next(it)) #print value using iteration function
print(next(it))
print(it.__next__()) #print value using iteration function  '''

'''
# Iterating over a list
print("List Iteration")
l = ["geeks", "for", "geeks"]
for i in l:
    print(i) '''

'''
class Fun:
    def __iter__(self):

        self.a=1
        return self
    def __next__(self):
        x = self.a
        self.a+=1
        return x
my = Fun()
ite=iter(my)
print(next(ite))
print(next(ite))
print(next(ite))
print(next(ite))
print(next(ite))
print(next(ite))
print(next(ite))
print(next(ite))'''

'''
class Infilter:
   
    def __iter__(self):
        self.num = 1
        return self

    def __next__(self):
        num = self.num
        self.num += 2
        return num

a=iter(Infilter())
print(next(a))
print(next(a))'''

'''
i=[1,2,3,4,5]
h=iter(i)
print(next(h))
print(next(h))
print(next(h))
print(next(h))
print(next(h))'''

'''
# A simple generator function
def my_gen():
    n = 1
    print('This is printed first')
    yield n

    n += 1
    print('This is printed second')
    yield n

    n += 1
    print('This is printed at last')
    yield n

for item in my_gen():
    print(item)  '''

'''
class A:
    def __iter__(self):
        self.a=1
        return self
    def __next__(self):
        b =self.a
        self.a +=2
        return b


obj=iter(A())
print(next(obj))
print(next(obj))'''
'''
num=0,1,7,9
i=iter(num)
print((i))#for type
print(next(i))'''
'''
a = [1,2,3]  
b= ['a', 'b', 'c']  
c = zip(a,b)  
d=iter(c)
print(next(d))
print(next(d))'''
'''
import itertools  
print("Printing the number repeadtly:")  
print(list(itertools.repeat(40,15)))  '''
'''
import itertools
print(tuple(itertools.repeat("hello",5)))'''

'''
def simpleGeneratorFun():
    yield 1            
    yield 2            
    yield 3            
   

value = simpleGeneratorFun() 
print(value.__next__())
print(value.__next__())
print(value.__next__())'''
'''
def fib(limit):
    a,b=0,1
    while a<limit:
        yield a
        a,b=b,a + b
x = fib(5)
print(x.__next__())
print(x.__next__())
print(x.__next__())'''

'''
iterable_value = iter('Geeks')
while True:
            try:

                            # Iterate by calling next
                print(next(iterable_value))
		
            except StopIteration:

                            # exception will happen when iteration will over
                print("\nstop iteration")
               break '''
'''
def f1():
    n=0
    print("new")
    yield n + 1
a=f1()
print(next(a))'''
'''
def generator_thr_iter():
   yield 'xyz'
   yield 246
   yield 40.50
for i in generator_thr_iter():
   print(i)'''
'''
list = [1,2,3,4,5,6,7]  
tuple = (1,2,3,4,5,6,7)
z = [x**3 for x in list]  
   
a = (x**3 for x in tuple)  
  
print(z)

print(a)'''

'''
#print sq of top 10 values
def f1():
    n=0
    while n < 10:
        sq=n**2
        yield sq
        n+=1

obj =f1()
print(obj.__next__())
print(obj.__next__())
print(obj.__next__())
print(obj.__next__())
for i in obj:
    print(i)'''

def even():
    n = 0
    n+=2
    yield n

    n+=2
    yield n

    n+=2
    yield n

obj =even()
print(obj.__next__())
print(obj.__next__())
print(obj.__next__())
try:
    print(obj.__next__())

except Exception:
    print("faild")


