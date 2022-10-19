'''

#2 given sample dictionary -how would you update value 'apple' from 10 to 100
fruit = {'apple':10,'oranage':20,'banana':30,'guava':50}
fruit['apple']=100
print(fruit)


#3 how would you find common element present in given two sets
s1={2,5,6,8,3,9}
s2={1,5,9,2,3,4}
print(s1.intersection(s2))

#4implement logic to check if no is palindrome or not
n=int(input('enter no:'))
temp = n
rev =0
while n>0:
    dig = n%10
    rev =rev * 10+dig
    n = n//10
#5 print('it is not palindrome')
if (temp == rev):
    print('the numb is palindrome')'''
'''
#5 write prog for print 123 pattern
for i in range(6):
    for j in range(i):
        print(i,end=' ')
       
    print(' ')

#6 write prog for print # pattern
for i in range(6):
    print(i)
    for j in range(i):
        print('#',end =' ')
    print('')

def pattern_print(n):
    for i in range(0,n):
        print(i)
        for j in range(0, i+1):
            print('#',end =' ')
        print('')
pattern_print(6)        

#7 write for i in range(6): # control row 
    for j in range(i): # control printing nos
        print(j,end =' ')
    print('')        
'''
'''
 # 9 write prog for 123 pattern 
for i in range(6):
    for j in range(i):
        for k in range(j):
        #print('i',i , end =' ')
            print(j,end=' ')
    print('')
    
# print pattern for AABABC
char = 65
for i in range(0,5):
    for j in range(0,i+1):
        
        print(chr(char),end =' ')
    char +=1    
    print('')    '''

# print abcd upto z in pattern
char = 65
for  i in range(0,7):
    for j in range(0,i+1):
        print(chr(char),end=' ')
        if char == 90:
            break
        char+=1
             
    print('')    

    
'''
# calculate simple interest
p =int(input('Enter principle value:'))
pr=int(input('Enter period of time'))
i=int(input('Enter interest'))
simple_interest = p*pr*i/100
print('simple_interest is:',simple_interest)

#7 calculate compound interest

def compound_interest(principle_amount,rate,time):
    amount = principle_amount*(pow((1+rate/1000),time))
    ci= amount - principle_amount
    print("compound interest is:",ci)

compound_interest(10000,5.5,5)'''
'''
# print all prime no is in interval

start=1
end =20
for i in range(start,end+1):
    if i >1:
        for j in range(2,i):
            if (i % j == 0):
                break
            else:
                print(i)


# find area of circle
def findArea(r):
    pi=3.14
    return pi*(r*r)
print('area of circle is :',findArea(5))

# nth fibonacci no
def fibonacci(n):
    if n <=0:
        print('incorrect input pleas enter greater than zero')
    elif n ==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci (n-1)+fibonacci(n-2)
    

print(fibonacci(15))'''

# check no is fibonacci or not


# print for sum of square of 1st n natural no
sm=0
for i in range(5):
    p=i*i
    sm=p+sm
print(sm)
    

# prog for cube sum of 1st n no's.
def sumOfcube(n):
    sum=0
    
    for i in range(1,n+1):
            sum +=i*i*i
    return sum

print(sumOfcube(5))    

# prog for sum of array

def sum_array(arr):
    sum =0
    for i in arr:
        sum=sum+i
    return sum    

a=[12,13,14,15]
print(sum_array(a))    


#prog for find min sum of factor
def findmin(sum):
    sum = 0
    num =12
    i=2
    while (i *i<=num):
        while(num % i==0):
            sum+=i
            num/=i
        i+=1
        sum+=num
        return sum


num=12
print(findmin(num))    


#

def binaryPalindrome(num):
    binary = bin(num)
    binary = binary[2:]
    return binary ==binary[-1:-4:-1]

num =10
print(binaryPalindrome(num))
    

#















    
