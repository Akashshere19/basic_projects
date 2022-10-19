'''
# prog for multiline input

import sys
msg = sys.stdin.readlines()
print(msg)

#print items with index
f=[9,6,7,5,4,5]
for v,i in enumerate(f):
    print(v,i)
    
#how to different instance variables from class variable

class myClass:
    def __init__(self): 
        self.varInst = "this is instance variable"
        
    varClass ="this is class variable"
    

obj=myClass()
print(obj.varClass)
print(obj.varInst)

myClass()'''


# example of list comprehensive
'''
l=[x*2 for x in range(1,6)]
print(l)
l.append((22,23,27))
print(l)
l.extend((23,45))
print(l)
print(l[5][1])
print(l) '''
'''
st="hello world"
for i in st:
    print(i[::-1],end='')

print(st[::-1])



l=[2,7,5]
print(id(l))
l.append(3)
print(l)
print(id(l))


t=(2,4,5,5)
print(t)
print(id(t))
l1=sorted(t)
print(l1)
l1.append(12)
print(l1)
print(tuple(l1))
print(id(l1))

p=[12,2,35,]
p[2]=22
print(p)
r=(12,3,58)
r[3]=232
print(r)
# fabonicci series
def f1(n):  
    a,b=0,1
    while a<n:
        print(a,end=' ')
        a,b =b, a+b
    print()    

f1(10)




# fabonacci
a,b=8,13 # starting two values 

while a<200: # 200 is end value
    print(a)
    a,b=b,a+b # b will print hence copy of b value in a
print()    
    '''
'''
# * star pattern in square

for i in range(6):
    for j in range(6):
        print('*',end=' ')
    print('')    

#satr in incresing pattern
n=7
for i in range(n):
    for j in range(i+1):
        print('*',end=' ')
    print()   


# star pattern in decresing

n= 6
for i in range(n):
    for j in range(i,n):
        print('*',end=' ')
    print()


'''
'''
# star pattern in 


n=6
for i in range(n):
    for j in range(i,n):
        print(' ',end=' ')
   # print()
#for i in range(n):
    for j in range(i+1):
        print('*',end=' ')
    print()




# star 

n=6
for i in range(n):
    for j in range(i+1):
        print(' ',end=' ')
    for j in range(i,n):
        print('*',end=' ')
    print()  '''  
'''  
#
n= 6
for i in range(n):
    for j in range(i,n):
        print(' ',end=' ')
    for j in range(i):
        print('*',end=' ')
    for j in range(i+1):
        print('*',end=' ')
    print()   

#
n=6

for i in range(n):
    for j in range(i+1):
        print(' ',end=' ')

    for j in range(i,n):
        print('*',end=' ')
    for j in range(i,n-1):
        print('*',end=' ')
    print()   '''  
'''        
for i in range(6):
    for j in range(i):
        print(' ',end=' ')
    for j in range(i,6):
        print('*',end=' ')
    print()'''

'''
for i in range(6):
    for j in range(i):
        print('*',end=' ')
    print()

for i in range(6):
    for j in range(i,6):
        print('*',end=' ')
    print()'''

'''
    
*
**
***
****
*****
******
*****
***
**
*
'''
'''
      *
     **
    ***
   ****
  *****
 ******
  *****
    ***
     **
      * '''

'''
for i in range(6):
    for j in range(i,6):
        print(' ',end=' ')
    for j in range(i):
        print('*',end=' ')
    print()    

for i in range(6):
    for j in range(i):
        print(' ',end=' ')
    for j in range(i,6):
        print('*',end=' ')
    print() '''

'''
* * * * * * * 
* * * * * * * 
* * * * * * * 
* * * * * * * 
* * * * * * * 
* * * * * * * 
* * * * * * *  '''      

'''
for i in range(7):
    print('* '*7)'''
'''
* 
* * 
* * * 
* * * * 
* * * * * '''
'''
for i in range(6):
    print('* '*i) '''
'''
            
          * 
        * * 
      * * * 
    * * * * 
  * * * * * 

for i in range(6):
    print('  '*(6-i)+ '* '*(i)) '''
'''
     * 
    * * 
   * * * 
  * * * * 
 * * * * *
for i in range(6):
    print(' '*(6-i)+'* '*i)'''

'''
* * * * * * 
 * * * * * 
  * * * * 
   * * * 
    * * 
     * 
for i in range(6,0,-1):
    print(' '*(6-i)+'* '*i) '''
'''
     * 
    * * 
   * * * 
  * * * * 
 * * * * * 
* * * * * * 
 * * * * * 
  * * * * 
   * * * 
    * * 
     * 

for i in range(6):
    print(' '*(6-i)+'* '*i)

for i in range(6,0,-1):
    print(' '*(6-i)+'* '*i) '''

'''
* 
* * 
* * * 
* * * * 
* * * * * 
* * * * * * 
* * * * * 
* * * * 
* * * 
* * 
*     
for i in range(6):
    print('* '*i)

for i in range(6,0,-1):
    print('* '*i)
'''
'''
for i in range(6,0,-1):
    print(' '*(6-i)+'* '*i)
for i in range(6,0,-1):
    print(' '*(i)+'* '*i) '''





'''   *
     **
    ***
   ****
  *****
   ****
    ***
     **
      * 


for i in range(6):
    print('  '*(6-i)+'* '*i)
for i in range(6,0,-1):
    print('  '*(6-i)+'* '*i)'''     
'''

stdno=int(input('Enter student no:'))
stdname=input('Enter Student name:')
mrs1=int(input('Enter mark of sub1:'))
mrs2=int(input('Enter mark of sub2:'))
mrs3=int(input('Enter mark of sub3:'))
mrs4=int(input('Enter mark of sub4:'))
mrs5=int(input('Enter mark of sub5:'))
mrs6=int(input('Enter mark of sub6:'))
total=mrs1+mrs2+mrs3+mrs4+mrs5+mrs6
avgm=total/6
print('total mark of sub1:',mrs1)
print('total mark of sub2:',mrs2)
print('total mark of sub3:',mrs3)
print('total mark of sub4:',mrs4)
print('total mark of sub5:',mrs5)
print('total mark of sub6:',mrs6)
print('Total mark of All Sub:',total)
print('Average mark of all sub is:',avgm)'''
import pickle
d={}
d['id']=1257
d['name']='obama'
d['salary']=290439.0494
print(d)
bs=pickle.dumps(d)
print(bs)

f=open('employ.pickle','wb')
f.write(bs)
f.close()
print('done')
    
print(employ.pickle)

