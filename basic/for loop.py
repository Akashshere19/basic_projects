'''
x= (i for i in range(3))
for j in x:
    print(j)

y= (i for i in range(5))

for j in y:
    print(j) '''


'''
x = 9
for i in range(2,x):
    if i % 2 == 0:
            print('not a prime number:',i)
    else:
        print('prime number:',i) '''
'''
data = [1,2,3,8,7]
for index, value in enumerate(data):
    print(index, value)'''
'''  
data = {'First Name': 'Akhilesh', 'Last Name': 'Singh'}
 
for key, value in data.items():
    print(key, value)'''

'''
for count in range(10):
    if count == 5:
        print('five is skip')
        continue # only skip value of 5
        
    print(count)

for count1 in range(10):
    if count1 == 5:
        print('five is pass') # pass will not skip 5 
        pass 
    print(count1)

for count2 in range(10):
    if count2 == 5:
        print('five is braek')
        break
    print(count2)'''

    
'''
f=['a','b','c']
for i in f:
    print(i) # here b will print becoz print i before if statement
    if i =='b':
        print('stop here')
        break'''
'''  
x='geeksforgeeks'
print(x)
for letter in x :

    if letter == 'e' or letter == 's':
        continue # 'e' and 's' will skip or avoid
    print('Current Letter :', letter) ''' 
'''
for i in range(10):
    print(i, end=" ")
print('...')'''
'''
l=[1,2,3,4,5,7,7,7,7,8,9,0]
for i in range(len(l)):
    print([i],end='')'''
'''   
sum=0
for i in range(1,13):
    sum=sum+i
    print(sum)
print("\n",sum)'''

'''
l=['akash','shere','santaji','nagar']
for i in range(len(l)):
    print([i],l[i])'''
'''
from time import sleep

for num in range(10,20):     #10 11 12 13 14 15 16 17 18 19
   for i in range(2,num):  # 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 
      if num%i == 0:    # 10 /2 = 0    
         j=num/i             
         print ('%d equals %d * %d' % (num,i,j))
         sleep(1)
         break
          
   else:
      sleep(1)
      print (num, 'is a prime number')'''

for n in range(10,30):
               for i in range(2,n):
                   if n % i==0:
                       j =n/i
                       print('%d equal %d * %d' %(n,i,j))
                       break
               else:
                   print(n,'is prime')



      
'''
numbers = [6, 5, 3, 8, 4, 2, 5, 4, 11]

sum = 0

for val in numbers:
    sum = sum+val

print("The sum is", sum)

digits = [0, 1, 5]

for i in digits:
    print(i)
else:
    print("No items left.")

student_name = 'Soyuj'

marks = {'James': 90, 'Jules': 55, 'Soyuj': 77}

for student in marks:
    print(student)
    if student == student_name:
        print(marks[student])
        break
else:
    print('No entry with that name found.')



d={1:'apple',2:'ball',3:'cat',4:'dog'}
for i in d:
    
    print(i),print(d[i])

l=['akash','ball','dog']
for i in l:
    
    if 'b' in i:
        break  #continue,#break
    print(i) 

for i in ['a','b','c','d','e']:
    print(i)
    
else:
    print("done")

for i in range(10):
    print(i)
    
else:
    print("done")
    
mydictionary = {'name':'python', 'category':'programming', 'topic':'examples'}

for x in mydictionary:
	print(x, ':', mydictionary[x])

for x in range(2, 10):
    if(x==7):
        break
    print(x)
    
print("loop stop") 

for i in range(2,10):
    print(i)
print("out of loop")
for i in range(5):
    #print('x',end='')
    for i in range(6):
        print('x',end='')
    print()'''

l=['akash','shere','santaji','nagar']
for i in range(len(l)):
    print([i],l[i])


# star pattern

for i in range(1,10):
    for j in range(1,i,1):
        print('*',end=' ')
    print(' ') 













