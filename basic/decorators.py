# decorator is a function that is take function as a arguments
        #and give return as function



'''def func1():
    print('hello')
func2=func1
del func1
print(func2)'''

'''
# return function by function
def funcret(num):
    if num == 0:
        return print
    if num ==1:
        return int
a = funcret(0)
a1=funcret(1)
print(a1)
print(a) '''

'''
#function is an argument
def exe(func):
    func('hello')
    
exe(print)'''
'''
#decorator example
def dec1(func):
    def now():
        print('statement1')
        func()
        print('statement2')
    return now
@dec1
def hall():
    print('statement')

hall()


#decorator example
def dec1(func):
    def now():
        print('statement1')
        func()
        print('statement2')
    return now
@dec1
def hall():
    print('statement1')
#hall = dec1(hall)
hall() '''

'''
def result(marks):
    for  m in marks:
        if m >= 33 :
            pass
        else:
            print('fail')
            break
    print('pass')
result([64,98,35,87,65,54])  '''      
            

'''
def distiction(result1):
    def result_dis(marks):
        for m in marks:
            if m > 75:
                print('Distinction',m)
        result1(marks)
    return result_dis
    
@distiction

def result(marks):
    for  m in marks:
        if m >= 33 :
            pass
        else:
            print('fail',m)
    print('other sub pass')       
   
result([64,98,35,87,65,32]) '''

'''
def f1(n):
    def f2():
        print('hi')
        n()
        print('hello')
    return f2      
@f1        
def f3():
    print('gujrat')
    


f3() '''

'''
def dis(res):
    def res_dis(marks):
        for m in marks:
            if m >=50:
                print('you are ginius',m)
            res(marks)
    return res_dis  

@dis 

def result(marks):
    for m in marks:
        if m > 35:
            pass
        else:
                print('fail',m)
                break
           
        print('pass',m) 
            
        
result([23,98,56,34,32]) '''

'''
import time
def timer(func):
     def inner(*args, **kwargs):

             t1 = time.time()
             f = func(*args, **kwargs)
             t2 = time.time()
             print('Runtime took {0} seconds'.format(t2-t1))
             return f
     return inner
@timer
def example_function():
 #do stuff
    pass
example_function() '''

'''
def sh(tex):
     return tex.upper()
print(sh('hello'))
yel=sh # func treat as a object
print(yel('hello'))'''

'''
def shout(text):
     return text.upper()
def wish(text):
     return text.lower()
def greet(fun):
     y=fun('hello')
     print(y)
obj=shout('hello')
print(obj)
print(wish('AKASH'))

d=greet(shout) # here shout func as a argument '''
'''
def outer_dec(func):
     def inner():
          print('this one is inner')
          func()
          print('this is second')
     return inner
def used_func():
     print('this is used function')
used_func = outer_dec(used_func)
used_func()'''

'''
def f1(f):
     print('outer')
     def f_inner():
          f()
          print('this is hello')
     return f_inner
@f1
def f2():
     print('this is second')

#f2 = f1(f2)
f2() '''












        
    
