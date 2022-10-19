'''s=set()
print(s)
print(type(s))
d={}
print(type(d))'''
#add:add 1 element in there position
s={3,9,2,4}
s.add(None)
print(s)
#update :update element or another tuple,list
s={8,9,6,4}
s.update({6,9,5})# not allow duplicate items
s.update([1,9,7,5])
l=[7,0,98,56]
s.update(l)
print(s)

#union : concatinate to two set
s={9,6,4,3}
s1={2,1,3}
print(s.union(s1))
print(s.union((2,5,1)))
print(s.union({3,98,76}))
#copy : copy set to another variable
#pop : cut one last element from set
s1={2,9,7,5,4}
s1.pop()
s1.pop()
s1.pop()
s1.pop()
s1.pop()
print(s1)
set={6,9,4}
set.pop()
print(set)
#remove : delete given item
'''
set1={2,9,4,7,1,3}
set1.remove(3)
set1.remove()
print(set1)'''
#discard : delete givem item if not available then doesn't show keyerror
set={2,10,22,34}
s.discard(34)
print(set)
#clear :total set will be delete
#difference
s={2,9,6,89,78}
s1=s.difference({98,78,9,6})
print(s1)
#difference_update
s2={12,98,67,67}
s2.difference_update({23,98,67,2,3,8})
print(s2)
#intersection

#intersection_update

#isdisjoint
#issubset
#issuperset

#symmetric_difference
#symmetric_difference_update
'''
s={2,1,3,4,11,7,8,5}
s1={1,3,4,33}
print(s.symmetric_difference((1,2,3,88,43,56,20)))
'''

'''
s={3,5,6,2,5,7}
s.remove(2)# remove takes value
s.discard(2)# discard also takes value but not available that time not showing error
print(s)'''
'''
s={3,2,8,4}
s.clear()
print(s)'''
'''
s={5,8,3,2}
s1={5,6,7,2}
s3=s.difference(s1) # showing different element in both set
print(s3)'''
'''
s={2,8,4,3,1}
s1={9,4,2,7}
s.difference_update(s1)
print(s)'''

'''
s={2,8,4,3,1}
s1={9,4,2,7}
s2=s.intersection(s1) # showing common element in both set
print(s2)'''

'''
s={2,6,1,5,3}
s1={12,5,7}
s.intersection_update(s1)
print(s)'''


'''
s={2,6,8,9}
s.add((1,6,7)) # diff bet add and update is same as append and extend
s.update((1,6,7))
print(s)'''

'''
s={2,7,8,3}
print((s))
print(s.union((3,4,5)))
print(s)'''



'''
s={13,4,68,5}
s.add(12) # add one element
s.add((11,12)) # only tuple not for list taken as one element
print(s)
s.update([12,78]) # add many item 
print(s)
s1={21,98,67}
print(s1.union(s))
s2=s1.copy()
print(s2) '''

'''
s={1,4,6,7}
s.discard(12) # it will not give error
s.remove(12) # will give error
del(s[2])
print(s)'''

'''s={12,18,10,16}
s.clear()

print(s)'''

'''
s={1,'a',29,36,3}
s1={9,3,5,2,7}
print(s.difference(s1))

print(s)
print(s1) '''
'''
s1={1,9,3,4,2,5}
s2={2,5,6,7,8}
print(s1,s2)
s1.difference_update(s2)

print(s2)
print(s1) '''

'''
s1={1,9,3,4,2,5}
s2={2,5,6,7,8}

print(s1.intersection(s2)) # it will not chnage in original list
print(s1)
s1={1,9,3,4,2,5}
s2={2,5,6,7,8}
s1.intersection_update(s2) 3#it will be definatly change in original list 
print(s1) '''


'''
s={12,13,19,16}
s.add((14,15))
print(s)
s1=(12,17,199,167)
s2=(10,17)
s.add(s2)
s.update(s1)
print(s)'''




'''
s={'cherry','banana','graps','apple',2,2,'cherry',3}
print(s)
print(type(s))
s.add('lichi') # add new item in 
print(s)
s1={'lichi','papaya'}
s1.update(s) # update another set in old set 
print('update:',s1)

s.union(s1) 
print('new:',s)'''

'''
s.{remove('lichi')
print(s)
print(s.remove('banana'))

print(s) '''

'''
s={'banana','cherry','apple','mango','pinaple'}
s1={'pirrot','kurry'}
print(s.union(s1)) # add two sets and create new set
s3=s.union(s1) # add two sets and create new set
print(s3)'''

'''
s={'happy','marriage','life'}

s1=s.copy()# copy and paste set s in set s1
print(s)
print(s1) '''

'''
s={'banana','karela'}
print(s.pop())
s1=(s.pop()) #remove 1 item frm array but we can paste to other var
print(s1)
'''

'''
s={'apple','lemon','watremilon'}
s.remove('apple') # it remove by given item name
print(s) '''

'''
s={'set','superset','tuple'}
s.clear() # clear all set
print(s) '''

'''
s={1,2,5,3}
s1={5,8,4,6}
s3=s.difference(s1)# show those element not present from s in s1
s4=s1.difference(s) # show those element not present from s1 in s
print(s3)
print(s4) '''

'''
s={1,2,5,3,9,3.5}
s1={5,8,4,6}

s.difference_update(s1) # print those element not present in s
s1.difference_update(s) # print those element not present in s1
print(s)
print(s1) '''

'''
s={1,2,3,7}
s.discard(2) # delete or remove element
print(s) '''

'''
s={'a',3,2,4,6,'b'}
s1={3,9,5,0.3,'c'}
#p=s1.intersection(s)
print(s.intersection(s1)) # create new set those elements are common in both set

'''

'''
s={2,4,5,6,9,7}
s1={2,7,9,8,4,5,6,4}
s2={2,8,9,4,6}
p= s.intersection_update(s1,s2)
print(p)
print(s1)
print(s2)
print(s) '''

'''
s={2,7,9,3}
s1={2,4,3,9}
p=s.intersection_update(s1) # update common element in both set
print(s)
print(s1) '''

'''
s={2,7,4,3,2,9}
s1={2,7,4,8}
s2={'a','b','c'}
print(s.isdisjoint(s1)) # check diff item and give output in boolean
print(s.isdisjoint(s2))
print(s.isdisjoint(['n','p'])) # check set with list,tuple,
print(s.isdisjoint(('m','u')))

a={'akash'}
print(a.isdisjoint('akash'))'''

'''
s={2,7,5,3}
s1={1,'a',9,7,4,3,2,6}
print(s.issubset(s1)) # check all elements of s in s1 

s={2,4,5,6}
s1={2,8,4,5,7,9,6}
print(s.issubset(s1)) '''


'''
s={2,9,30,4,5,6}
s1={2,4,5,6}
print(s.issuperset(s1)) # check all elements of s1 are available in s

'''

'''
s={2,8,3,4,6}
s1={2,8,4,3,7}
print(s.symmetric_difference(s1))'''

'''
p=s.symmetric_difference_update(s1) 
print(s)
print(s1)'''

'''
s={1,2,3,4}
s1={4,5,6}
print(s.symmetric_difference_update(s1),s)

'''


'''
s="akash shere from akola DIFFICULT"
print(s.title())

fruits=['apple','grapes','orange']
print('Original List:')
print(fruits)
fruits = [i.title() for i in fruits]
print('List after capitalizing each word:')
print(fruits) 


s='akash shere akola'
result = ' '.join(i.capitalize() for i in s.split())
print(result) '''



'''

#calculate repeated character comes in string
s = "ABBBBCCCCCCCCAB kzxcA"
d = {i:0 for i in s}

for i in s:
    d[i]+= 1
print(d)

s="akash shere"
e= {k:0 for k in s}
for k in s:
    e[k]+=1
print(e)    '''
'''
s={2,4,5,6}
print(max(s))
print(5 in (s))'''
'''
#find s1 and s2 is equal
s={2,3,4,6}
s1={1,8,3}
print(s==s1) '''
'''
# set output pront in itration
s={1,2,4,6,7,9}

d={i:0 for i in s}
for i in s:
    d[i]+=1
    print(d) '''

'''
s={1,5,6,7,8}
s1=[1,3,55]
s.update(s1)
s.update({12,44,55,22,33})

print(s) '''
'''
#assign operator (=)
s={1,2,4}
s1=s
s1.add(12)
s.update([12,34,23])
print(s,s1)
print(s)

# shallow operator
s={1,3,5,8}
s1=s.copy()
s1.update([12,34,67])
print(s1)
print(s)

# deep copy
import copy
s={1,3,2}
s1=copy.deepcopy(s)
s1.update([12,13,14])
s1.add((1,2,3)) # we can use tuple in set but not list becoz list or set is unhasheble
#s1.add([18,14,16])

print(s1)

print(s) '''

'''
s={2,7,4,6}
s1={9,2,3,}
w=s.union(s1)
print(w) '''
'''
s1={9,2,3,}
w=s1.union({13,45,64})
print(w)
print(s1.union([12,14,15]))'''

'''
s={5,6,7}
s1=s
s2={1,12,2}
print(s1.union(s2)) # not change in s when union add in 
print(s) '''

'''
s={1,2,3}
print(s.union([4,5,6]))
print(s.pop())
p=s.pop()
print(p)

s={1,2,3,4,5}
(s.remove(3))
s1=s.remove(4) # directly delete item 
print(s1) # not allow to store in another variable
print(s) '''

'''
s={1,2,3,4,5}
s.remove(5)
print(s) '''


'''
s={1,2,3,4,5}

s.discard(44) # if element not available the doesn't make noice or error
s.remove(44) # if element not available the does make noice or show error
print(s) '''

'''
s={1,2,3,4,5,6,7,8,9}
s.pop()
s.remove(9)
s.discard(8)
s.pop()
s.remove(7)
s.discard(6)
s.pop()
print(s)'''
'''
s={1,2,3,4,5,6,7,8,9}
s1={2,4,6,8,9,3}
print(s.difference(s1))
s.difference_update(s1)
print(s)'''






