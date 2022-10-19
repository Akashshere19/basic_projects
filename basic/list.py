#print([m for m in dir(list) if not m.startswith('__')])
#print([m for m in dir(tuple) if not m.startswith('__')])
#print([m for m in dir(set) if not m.startswith('__')])
#print([m for m in dir(dict) if not m.startswith('__')])

#print([m for m in range(5)])

'''
l=[(1,'akash'),(2,'sham'),(4,'shoja')]

print(l,type(l))
l1=[4,'h',5.7,9,2,6]
t1={'a','b','n','o'}
l2=list(zip(l1,t1))
print(l2)
l7=[(1,3),(3,7),(9,4)]
print(list(zip(*l7)))'''

'''
l=list((12,12,13,14,15,16,17,18,19))
print(l)
print(l[-4:-1])
print(l[-1:-4:-1])
l[1:3]=89,98
l.append(9) 
l.append([1,9,12])
l.insert(5,12)
l.extend([5,0,12])
print('extend:',l)

l.remove(12)
print("this is remove:",l)

del l [3]
print(l)

l.pop(5)
print('pop :',l)

l=(1,12,13,)
print(list(l))'''
'''
l=[1,9,2,8,3,7,4,7,6]
i=0
while i< len(l):
    print(l[i])
    i=i+1
    
#print("\n")
for j in l:
    
    print(j,end="")
    
print("\n")
[print(x) for x in l]

newlist = [x for x in range(10)]
print(newlist)

l=['hjh','apple','lk','ball','uo']
n=[]
for i in l:
    if 'a' in i or 'b'in i:
        n.append(i)
        
print(n)

number=[1,2,3,4,5,6,7,8,9]
x=[num*num for num in number]
print(x)

for i in number:
    if i%2==0:
        print("even :",i)
a=lambda number,i:'even' if i%2==0  else 'odd'
print(a)'''

'''
l=[1,2,3,4,5]
l.extend([7])
l.extend(['eight',9,10])
l.extend([6.8])
print(type(l[6]),type(l[5]),type(l[9]))
print(l)'''
'''
l=[1,2,3]
l.append(2)
print(l)
l.append([2,9])
l.extend([2,9])
l.insert(2,9)
print(l)
l=[1,4,6,9]
l.extend([1])
l.insert(2,20)
print(l)

l=[1,9,8,3]
print(l[::-1])
p=reversed(l)
l.reverse()
print(l)
l=[2,7,7,5,4]
print(l.count(7))

l=[2,9,4,8]
(l.sort())
print(l)

l=[9,3,4,5]
l.clear()
print(l)
l.extend([1,3,9,2,3,4,7])
print(l)
print(max(l))
print(min(l))
print(l.index(4))
p=list((1,9,2,4))
print(p)
l=[5,8]
j=[7,9]
l.extend(j)
print(l)'''




'''
# pride institute

#list define by two way
li_item = list(['banana','apple','watermillon','cherry','guava']) #1st way
li_two = ['banana','apple','watermillon','cherry','guava'] #2nd way
print(li_item)
print(type(li_item))
print(li_two)
print(type(li_two)) '''

'''
li_item = list(['banana','apple','watermillon','cherry','guava'])


print(li_item[0]) #print 1st item
print(li_item[0:4]) #print string of list
print(li_item[0:6:3])
print(li_item[-1:-6:-1]) #print negative item

li_item[4] = 'mango' #add item
li_item[1:3] = 'graps','tomato','flower' #add items
print(li_item) '''

'''
li_item = list(['banana','apple','watermillon','cherry','guava'])

print(li_item.append('kiwi')) # add item but in last position
print(li_item)

li_item.insert(3,'tomato') # add item on index based 
print(li_item) '''

'''
# take tuple and add new element in that tuple
t=(1,2,3,4,'akash',23.5) 
print(t,type(t))
l= list(t)
print(l)

l.append('shere') 
print(l)
t= tuple(l)
print(t) '''


#append() :it append or add item to end of list
l=[2,9,3,4,5,7]
l.append([99,89])
l.extend([23,98,76])
l.insert(2,[23,98,76])
print(l)
del(l[6])
print(l)

l1=l.pop(2)
print(l1)
l.remove(5)
print(l)

l1=l.copy()
print(l1)
print(l.count(4))
l.reverse()
print(l)
print(l.index(4))
print(len(l))

#insert() : insert add at index position i
#extend() : it is add new list to end of existing list

#del    : remove specified element in list
#pop()   : remove specified index and display removed item.after removing
           #remaining list items moved forward to fill index gap
#remove() : user can remove  specified item from a given list

#copy() : it is copy toatl list into new variable
#clear()  :clear existing list
#count()   :counts no of times value is repeated inside a list
#reverse() : reverse in 
#sort()  :sort in ascending order
#index() : print index position of elememt in list.
#len() :   print total no of element
'''
l=[2,8,4]
l1=[3,7,9]
l.append([3,8,9,2])
l.append(l1)
l.extend(l1)
print(l)
l.insert(2,'a')
print(l)'''
'''
l=[3,8,9,4,2]
l.pop() # if index no not then cut last digit
l.pop(1) # pop in take index no also
print(l) '''

'''
l=[2,9,4,5,6]
del(l[3]) # del takes index no
print(l)
l.remove(6) #remove takes value
print(l)
'''
'''
l=[6,9,3]
l.reverse()
print(l)
l[::-1]
print(l)'''
'''
st='akash shere'
s=st.split()
print(s)
print(len(s))
st='akash shere'
s=st.split('.')
print(s)
print(len(s))'''

'''
l=[23,7,89,32]
l.append(5)
print(l)
l=[12,13,13,14]
l.append(11)
l.insert(2,[12,13,11])
l.append([112,113,123])
l.extend([22,23,24])
del(l[2]) # it work on index base
l.remove(12) # it work on value base
q=l.pop()
print(l)
print(q)
l.reverse()
print(l)'''



'''
l=['a',2,'aksh',3.7,'shere',34,23.45]
print(l.append('23')) # add 23 but at last
print(l.insert(2,23)) # add 23 on given index 2 position
print(l.extend([3,27,29,[273,34],(2.3,56)]))
print(l)#it add more than 1 element
del(l[0])
print(l.pop()) #remove last element
t=l.pop()
print('this is t:',t) # pop value give to another variable
print(l.remove(34)) # remove elment
s=l.remove(2)
print('this is s:',s) # remove not give to another variable becoz it directly delete
print('total of 2 is:',l.count(2.3)) #count

print(l)
print(len(l))
print(l.index(3.7))

print(l) '''

'''
l=['a',2,'aksh',3.7,'shere',34,23.45]


print(l.count([2,'a'])) #count total 2 element in list
t=[1,7,2,4] 
(t.sort()) # arrange in ascending order
print(t)'''

'''
l1=[2]
(l1.extend(range(5)))
(l1.extend(range(2,5)))
print(l1)

l2=[2]*10
print(l2)

l3=[{1,2} for i in range(10)]
print(l3)

l4=[x*x for x in(2,3,4,5,6)]
print(l4)
print(type(l4))
'''
'''
sq=[]
for i in (2,8,4,6):
     sq.append(0,i*i)
print(sq)''' 
'''
x=5
y=0
try:
    x/y
    
except Exception:
    #print('sorry')
    for i in range(5):
        y+=1
        v=x/y
    print(v)
     break   
finally:
    y+=1
    a=x/y
    print('this is finally',a)'''

'''
x=9
y=0
try:
    x/y
except  Exception:
     if y==0:
         for i in range(5):
             print(i)
             x/y
             
finally:
        print('sorry')'''


'''
#check for palindrom
a = "aba"
a='akash'

print(a[::]==a[::-1]) '''
    

# shallow copy and = and deep copy
'''
# example for =
l1=[1,2,3,4]
print('old l1:',l1)
l2=l1
l2.append(23) # when we changes in l2 that time also changes in l1
l2.insert(2,44)
l2.extend([26])
l2[1]='as'
print('new l1:',l1) 
print('l2:',l2)'''


#example for copy
'''
l1=[1,3,4,5,6,7]
print('old l1:',l1)
l2=l1.copy()
print('old l2:',l2)
l2.append(12) # when we change in l2 that time doesn't changes in l1
l3=[12,13,15]
l2.extend(l3)
l2.insert(1,[12,13,14])
l2[0]='a'
print('new l2:',l2)
print('new l1:',l1) '''

'''
import copy

old_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
new_list = copy.copy(old_list)

print("Old list:", old_list)
print("New list:", new_list)'''

'''
l=[2,6,7,9]
l2=l
print(id(l),id(l2)) # = is assign on same loc of memory

#l1=[1,3,4,5,6,7]
l2=l.copy()
l2.append(12)
print('l2:',l2,id(l2))
print('l:',l,id(l))'''

'''
#deep copy
import copy
l1=[1,3,4,5,6,7]

l2=copy.deepcopy(l1)
print(id(l1),id(l2))
l2.extend([12])

print('l2:',l2,id(l2))
print('l1:',l1,id(l1))'''


'''
#deep copy
print('example of shallow copy')
import copy
l1 =[[1,3,6],[4,9,5],[7,3,0]]
l2=l1.copy()
l2.append(12)
l2[2][1]=0
print('l2',l2)
print('l1:',l1)

print('example of deep copy')
import copy
l1 =[[1,3,6],[4,9,5],[7,3,0]]
l2=copy.deepcopy(l1)
l2.append(12)
l2[2][1]=0
print('l2',l2)
print('l1:',l1)'''

'''
#shallow copy
l1 =[[1,3,6],[4,9,5],[7,3,0]]
l2=l1.copy()
l2.append(12)# when we used function of list that time nothing to change in l1
print('L2:',l2)
print('L1:',l1)
l2[2][1]=2.22 # but when we trying to nested list that time also change in l1
print('l2',l2)
print('l1:',l1)
'''
'''
import copy
l1 =[[1,3,6],[4,9,5],[7,3,0]]
l2=copy.deepcopy(l1)
l2.append(12)
print('L2:',l2)
print('L1:',l1) # when we used function of list that time nothing to change in l1
l2[2][1]=2.22 
print('l2',l2)
print('l1:',l1)# when we change through nested loop that also nothing change in l1
'''
'''
# assign operator ( = )
l1 =[[1,3,6],[4,9,5],[7,3,0]]
l2=l1
l2.append(12)
l2[2][1]=0
print('l2',l2)
print('l1:',l1) '''



'''
l=[1,3,2,4,5,6]
print(sorted(l, reverse = True))# print in ascending with reverse '''

'''
l1=[1,2,3,4,5,6,7,8,9,10]
l2=[2,3,4,5,6,7,8,9]
for i in l1:
    for j in l2:
        if j ==7:
            continue
        print(i*j)
    print("this is outside") '''


'''
s= frozenset([1, 2, 3, 4, 5])

s.append(2) # frozenset is same as set but it is immutable
s.insert(23)
print(s)'''

'''
def x(value,values):
    v = 1
    values[0]=33
    
y=3
v=[1,2,3]
x(y,v)
print(y,v[0]) '''
'''

l=[1,2,3,7,3,9]
print(l[:-1])

l1=[11,22,13]
l2=[11,21,33]
print(l1>l2)

l3=[2,3,4]
print(l3*2)

l3=[1,2,3,5,5,6,2]
print(l3.index(5)) '''

'''
l =[1,2,4,5]
l1=[1,2,5,4]
print(l==l1) # output False 

l={2,4,6,1}
l1={1,6,4,2}
print(l==l1) # output True '''

'''
l=('a#b#c#d'.split('#'))
print(l)
l1=[2,3,4,5,2,3,2]
print(l1.remove(2))

l2=[1,3,3,3,3,1]
m=l2[0]
ind=0
for x in range(1,len(l2)):
    if l2[x]>m:
        m=l2[x]
        ind=x
print(ind)    '''

'''
l=[1,5,9,2,7,3]
print(id(l))
l.sort() #work on same mem loc
print(l,id(l))'''

'''
l=[1,5,9,2,7,3]
print(id(l))
print(sorted(l)) #generate new memory loc
print(l,id(l)) '''

'''
#replace java by python
s="hello this is java"
s=s.split()
for i in s:
    if i == 'java':
        del(s[s.index(i)])
        s.insert(3,'python')
print(s)            
print(" ".join(s)) 

# or
s="hello this is java"

print(s.replace('java','python')) 

#or
s=['hello', 'this', 'is', 'python']
s.remove('python')
s.insert(5,'java')
s.append('world')
print(s)

print(','.join(s)) '''

'''

a=[12,23,34]
a.append((12,13))
print(a[3],type(a[3]))


a.extend([23])
a.extend((12,34,56))
print(a)
'''

'''
a=[12,13,14,14,11]
a.insert(2,[12,34]) # takes many item
print(a) '''


'''
s=[12,13,14,15,[12,117]]
s.pop([12,117])
print(s) '''
'''
s=[12,18,12]

print(s.count(12))
print(s.count(18)) '''

'''
# remove  integer value from string list
a=['aka','aky','babu',8,'shanya']
for i in a:
    if type(i)== str:
        print('it is string type')
    elif type(i) ==int :
        del(a[a.index(i)]) # a.index(i) will give the index of i in a
        #print('it is integer type')
print(a) '''

'''
#remove str from int list
import time
l=['akash',23,21,'rohan',2,29,12,19] # take a list
for i in l: # all item of list is iterate in i
    
    if type(i) == str: # find string type item
        
        del (l[l.index(i)]) # del str item
time.sleep(1)      
print(l)   # print remaining list '''

'''
list =['akash',9,'rohan']
result = ''
for element in list:
    result += str(element)
print(result)  



str =''.join(str(e) for e in list)
print(str) '''
'''
n= [i for i in range(20) if i%2 ==0]
print(n)
n=[i for i in range(50) if i%2==0 if i%3==0 if i %3==0]
print(n) '''

'''
l=[12,13,17,15,19]

if type(l) == list:
    l.sort()
    l.reverse()
         
print(l) '''
'''
# print only those no divide by 5 
numbers = [12, 75, 150, 180, 145, 525, 50]


for j in numbers:
    if j >500==0:
        break
    elif j>500:
        pass
    elif j%5 ==0:
        print(j,end=',') '''
'''
for index,item in enumerate(['one','two','three']):
    print(index,':',item)

x= (lambda e: e.upper(),['one','two','three'])
print((x))'''


'''   
l1= [(1,4,5),[2,4,6,5],(2.4,5.6,8.7)]
l=[(3,4),(2,3),(4,9)]
l1 and l.sort()
print(l,l1)'''

'''
# replace item in list
a=['a','b','z']
for i in range(len(a)):
    if a[i] == 'b':
        a[i] ='s'
    print(a)    
        
        
a=['hello','hi','hey']      
a[2]='namaste'

print(a) '''

'''
#add color with all items in list
a=['black','yellow','white']
a=[(item+ ' color') for item in a]
print(a)

#using lambda and map function
a=['black','yellow','white']
a=list(map(lambda item:(item + ' color'),a))
print(a)'''

'''
#whitw will replace by red
b=['black','yellow','white']
b[2:5] = ['red','orange','blue']
print(b)'''

'''
#only index 2 value print
l0=[2,3,4]
l1=[1,2,3]
l2=[6,7,8]
l=(l0,l1,l2)
f=[i[2] for i in (l1,l2,l0)]
print(f)
'''
'''
print('shallow copy:')
import copy
list=['red','blue',['yellow','orange']]
shallow_copy=list.copy()

print(id(list),id(shallow_copy))
print(list,shallow_copy)

shallow_copy[2][1]=('green')

print('shallow_copy:',shallow_copy,'list:',list)

print('deep copy:')
import copy
list=['red','blue',['yellow','orange']]
shallow_copy=copy.deepcopy(list)

print(id(list),id(shallow_copy))
print(list,shallow_copy)

shallow_copy[2][1]=('green')

print('shallow_copy:',shallow_copy,'list:',list)'''



'''
l=['orange','red','yellow','green']
print(l)
print(l.sort())
print(l)
l=['orange','red','yellow','green']
print(sorted(l,key=len))
l=['orange','red','yellow','green']
l.sort(key=len)
print(l)
'''
























