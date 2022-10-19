'''lst1 = [3,9,14,6,8,7,4,23,5]
print(lst1)
print(len(lst1))
print('-----------------')

for i in lst1:
    r = i * i
    print(r)

print('-----------------')
print(lst1)
print(len(lst1)) 
lst1 = [3, 9, 14, 6, 8, 7, 4, 23, 5]
print(lst1)
print(len(lst1))
print('-----------------')

for i in lst1:
    i = i * i
    print(i)

print('-----------------')
print(lst1)
print(len(lst1))
lst1 = [3, 9, 14, 6, 8, 7, 4, 23, 5]
print(lst1)
print(len(lst1))
print('-----------------')
i=0
while i < len(lst1):
    lst1[i] = lst1[i] * lst1[i]
    print(lst1[i])
    i+=1

print('-----------------')
print(lst1)
print(len(lst1))
fruits = ["Apple", "Orange", "Banana", "Peach", "grape", "Orange", "Banana"]
print(fruits)
print('-----------------------------------')
print(enumerate(fruits))
print('-----------------------------------')

for f in enumerate(fruits):
    print(f, type(f))

print('-----------------------------------')

for i,f in enumerate(fruits):
    print(i,'  --->  ', f)

fruits = ["Apple", "Orange", "Banana", "Peach", "grape", "Orange", "Banana"]
print(fruits)
print('-----------------------------------')
print(enumerate(fruits,start=25))
print('-----------------------------------')

for f in enumerate(fruits,start=25):
    print(f)

print('-----------------------------------')

for i,f in enumerate(fruits, start=25):
    print(i,'  --->  ', f)

lst1 = [3, 9,14, 6, 8, 7, 4, 23, 5]
print(lst1)
print(len(lst1))
print('-----------------')

for i,v in enumerate(lst1):  # (0,3),(1,9),(2,14),(3,6),(4,8),(5,7),(6,4),(7,23),(8,5)
    lst1[i] = v * v
    print(i,'------>', v)

print('-----------------')
print(lst1)
print(len(lst1))'''

'''
lst1 = [3, 9, 14, 6, 8, 7, 4, 23, 5]
print(lst1)
print(len(lst1))
print('-----------------')
#print(lst1 + 5)        # gives error
print(lst1 * 3)
print('---------------------')
"""
lt1 = [3,5,7]
lt2 = [4,6,9,7]
print(lt1 + lt2)""" '''
'''
l1=[]
while True:
    print('MENU')
    print('----------------')
    print('1. ADD A NEW ITEM')
    print('2. DISPLAY ALL ITEMS')
    print('3. DELETE AN ITEM')
    print('4. EXIT')
    ch=int(input('Enter your choice 1/2/3/4 :'))
    if ch==1:
        no=int(input(' Enter a new value to Add :'))
        l1.append(no)
    elif ch==2:
        print(l1)
    elif ch==3:
        if len(l1) >0:
            r=l1.pop(0)
            print(r, ' is deleted')
        else :
            print("No delete allowed from empty box")
    elif ch==4:
        break
    else:
        print('Invalid Option')
l1 = [6,8,9,3,4,5,9,5,2]
print(l1)
print(l1.index(9))

print('-------------------------')

l1.reverse() # the orizinal list is modified

print(l1)

print(l1.index(8))
lst1 = [4,6,9,3]
print(lst1)
print('--------------------')
a,b,c,d = lst1
print('a=',a)
print('b=',b)
print('c=',c)
print('d=',d)
print('--------------------')
print(lst1)'''
lst1 = [1,2,4,7,8,9]
lst2 = [1,2,4,7,8,9]
lst3 = [7,8,9,1,2,4]

print(lst1 == lst2)

print(lst1 == lst3)

print(lst1[:len(lst1)//2] == lst3[len(lst3)//2:])
print('==============================================')
print(lst1, type(lst1), id(lst1))
print(lst2, type(lst2), id(lst2))
print(lst3, type(lst3), id(lst3))
print(lst1 is  lst2)
    
























