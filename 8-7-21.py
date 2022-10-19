#Recursion 
"""
def sumnums(n):
    if n == 1:
        return 1
    return n + sumnums(n - 1)


print(sumnums(3))
print(sumnums(6))
print(sumnums(9))"""

"""
def factorial(x):    
     if x == 0:        
         return 1    
     else:        
         return x * factorial(x-1)
print(factorial(5))"""

'''
def print_sum(number):
    if number==1:
       return  1
    else:
       return number+print_sum(number-1)

print(print_sum(5))'''

"""
def sum_list(lst,length): 
    if length==0:
        return lst[0]
    else:
        return lst[length]+sum_list(lst,length-1)
lst=[1,2,3,4,5]
print(sum_list(lst,len(lst)-1))"""

"""
def positive_divisor(number,i):#6
     if number%i==0:
        print(i)
     elif number==i:
        return number
     return positive_divisor(number,i+1)
print(positive_divisor(6,1))"""

"""
def add_elements(e, lst): # adds the element to each list in the lst
    if lst == []:
        return []
    else:
        return [lst[0] + [e]] + add_elements(e, lst[1:])
print(add_elements('add',[['a'],['d'],['d']]))"""

"""
def div(f,s):
    value =f/s
    return value
output=div(f=10,s=2)
print(output)"""

"""
def div(f,s=2):
    v=f/s #10/2
    return v
out=div(10)
print(out)"""

"""
def add(*arg):
    t=0
    print(type(arg))
    for i in arg:
        t+=i
    return t
out=add(3,8,1,7,3)
print(out)"""

"""
def printMessage(message):
    print(message)

printMessage("Hello World")
printMessage("Hi!")
printMessage("How are you")"""

"""
def printMessage(name):
    return "Hello" + name

print(printMessage("shahid")) """

"""
def printNumber(number): #print decrising order
    print(number)
    if number == 0:
        return 0
    printNumber(number - 1)  

printNumber(5)"""
'''
def greet(name):
    print("Hello," + name + " Good morning!")
greet("akash")'''

'''
def absolute_value(num):
    """This function returns the absolute
    value of the entered number"""

    if num >= 6:
        return num
    else:
        return absolute_value(num-1)


#print(absolute_value(2))
print(absolute_value(5))'''


'''
def my_func():
	x = 10
	print("Value inside function:",x)

x = 20
my_func()
print("Value outside function:",x)'''
