# Arithmetic Operators
#addition
'''
a,b=2,6
print(a+b) #addition
print(type(a+b))
a=2
b=4.6
c=a+b
print(c,type(c))'''
'''
a=6
b=5
import operator
c=operator.add(a,b)
print(c)'''

'''
b=5
import operator

c=operator.add(6,b)
print(c)'''

#Subtraction 
'''
a=4
b=8
c=b-a
print(c,type(c))
x=2
y=4
c=x-y
print(c,type(c))
'''
'''
s=6
d=3
import operator
print(operator.sub(s,d))

s=8
import operator
print(operator.sub(s,7))'''
#Multiplication
'''
a=4
b=6
c=a*b
print(c)
import operator
c=operator.mul(a,b)
print("Using import Function:",c)'''
'''
print(3*'ab')
print(4*'a','b')
print(5*('a','b','c',))
print(5+'sj') # str and int not perform '''

#Division
'''
a=7
b=8
c=a/b
f=a//b
print(f)
print(c)

a=8
c=a/2 #showing float value
print(c)

a=8
c=8//2 #showing flat value
print(c)'''
'''
a=10
import operator
print(operator.truediv(a,2))
print(operator.floordiv(a,2)) #floor value show '''


#Modulus :it is showing remainder's value
'''
a=8
b=2
c=a%b
print(c)

a=8
b=3
c=a%b
print(c)

x=26

print(x%7)'''
'''
a=29
import operator
print(operator.mod(a,7))'''

'''
# Exponentiation Operator
x=2
y=3
z=x**y # x multiply with x 3 times 
print(z)

x=2
y=4
z=x**y # x multiply with x 4 times 
print(z)

x=4 #4*4*4*4
print(x**x)

x=5 #5*5*5*5*5
print(x**x)

x=5
y=2
print(x**y) # x multiply with x 2 times 
'''
# Membership operators
'''
x=(3,8,3)
y=(1,2,3)
print(x in y)
print(y in x)


a=('banaba','apple')
b=('apple')
print(b in a)

z=(2,9,3,6)
print(2 in z) '''

'''
x=(2,3,5,6,8)
print(10 not in x)

a=('apple','banana','cat')
b='dog'
print(b not in a)'''

# Identity Operators
'''
x='Apple'
y='aapke'
print(y is x)
print(y is not x) '''

# logical Operators
'''
a=2
b=3
c= a and b #01=0 11=1 10=0 00=0
print(c) '''
'''
a=2
b=3
c= a or b # 01 =1 10 =1 11=0 00=0
print(c)
'''
























