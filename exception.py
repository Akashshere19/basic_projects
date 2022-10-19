

a=6
b=0
c=7
try:
    print("ans=",a*b*c)
    for i in range(5):
        break
       
        
#except Exception:
                # print("it is not work")
finally:
    print("Bye") 
'''

try:
    a=eval(input("enter value"))
    b=eval(input("enter value"))
except Exception:
    print("pleas enter correct")
if a==int and b==int:
                try:
                    c=int(a/b)
                    print("ans=",c)
                except Exception:
                    print("You can not divide by zero")
                except NameError:
                    print("you can not type str")
    


                finally:
                        print("it is finally") '''

'''
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
    print("faild")'''
'''
amount =0
try:
    amount = int(input("enter an amount"))
except Exception:
    print("please enter correct value")    
    

if(amount>2999):
        print("You are eligible to purchase Dsa Self Paced")'''

'''
try:
    amount=00 #change to d
except NameError:
    print("type correct")
try:
    if(amount>2999):
              print("You are eligible to purchase Dsa Self Paced")

    print("amount is small")          

except NameError:
    print("syntax error please type correct")
    
    print("again")'''


from time import sleep
from threading import *

class Hi(Thread):
    def run(self):
        for i in range(5):
            print("hi")
            sleep(1)

class Hello(Thread):
    def run(self):
        
        for i in range(5):
            print("hello")
            sleep(1)

t = Hello()
t2=Hi()

t.start()
sleep(1)
t2.start()
t.join()
t2.join()
print("\nBye")
