'''x=1
while x<100:
    if x%10==3 and x%3==0:
            print(x)
    x+=1'''
'''n=int(input('enter a no:')) # not output shown
while n>0:
    r=n%10
    
    print(r,n/=10)'''
#Print count of the digits in the given number.

'''n=int(input('enter a no:'))
c=0
b=n
while n>0:
    n//=10
    c+=1
print('number of digit in {} is {}'.format(b,c))'''

# Sum of the digits in the number
'''
n=int(input('enter a no:'))
b=n
s=0
while n>0:
    r=n%10
    n//=10
    s+=r
print('sum of digits in {} is {}'.format(b,s)) '''   

# Magic number of the given number. Sum all the digits, until you get single digit sum
'''n= int(input('enter value:')) 
b=n
s=n
while s>9:
    n=s 
    s=0
    while n>0:
        r=n%10 
        s+=r
        n//=10
print('magic no of {} is {}'.format(b,s))'''

#printing number of factor of given number
'''n= int(input('enter a no:'))
i=1
c=0
while i <=n:
    if n %i==0:
        c+=1
    i+=1
print('number of factors of {} is {}'.format(n,c))'''

# Check the given number is perfect or not
'''n=int(input('enter a no:'))
i=1
s=0
while i<=n//2:
    if n%i==0:
        s+=i
    i+=1

if s==n:
    print('perfect')
else:
    print('not perfect')'''
#Print all perfect numbers below 100
'''
n=1
while n<=100:
    i=1
    s=0
    while i<=n//2:
        if n%i==0:
            s+=i
        i+=1
    if s==n:
        print(n)
    n+=1    
'''
#Check the given number is prime or not.
'''n=int(input('enter no:'))
i=1
c=0
while i<=n:
    if n%i ==0:
        c+=1
     i+=1
if c==2:
    print('prime')
else:
    print('not prime')'''

n=int(input('enter a no:')) # not output shown
while n>0:
    r=n%10
    
    print(r)
    n//=10














































        
