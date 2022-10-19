
#copy
#fromkeys : it will start given key
#get :show whatever item to output screen
#items :show all items
#keys :show all keys in output
#values : show values to output
#clear : delete all dict
#del :delete or remove given item or all dict
#pop :cut last item or given key no
#popitem  :cut last item or given key no
#setdefault: # give set item in output
#update : it is update on old items or add new items
'''
d={1:'a',3:'g'}
s={2:'s'}
d.update(s)
print(d)
d.update({4:'b'})
print(d)
d[5]='d'
print(d)'''

'''
d={1:'a',3:'g'}
l=[1]
p=d.fromkeys(d,l)
l.append(2)
print(p)'''


'''
d={1:'a',2:'d',3:'r'}
p=d.setdefault(3)
f=d.setdefault(4)
print(p) #will give r
print(f)# will give none becoz 4 is not available
print(d) '''

'''
d={1:'s','name':'akash'}
print(d)

print(d.fromkeys('abc',['akash','hello'])) # it will start key with a b c and value ['']
for i in d:
    print(i) '''






'''
d={1:'s'}
print(d)
print(type(d))
s={2:'d'}
d.update(s)
print(d)

print(d.keys())'''

'''
d={'name':'akash','no':'9766'}
p=d.get('no') 
print(p)

d={'name':'akash','no':'9766'}
p=d.keys() # get keys
print(p)

d={'name':'akash','no':'9766'}
p=d.items() # get items
print(p)


d={'name':'akash','no':'9766'}
p=d.values() #get values
print(p)

          
d['age']=26 # add key and value
print(d.keys())
print(d.items()) '''


'''
d={1:'akash',2:'akash',3:'akash'} #we repeat values but do not allow keys are repeated 
print(d)
d[2]='ram' # we changed values 
d[4]='rohit' # we can update items
print(d) '''

'''
d={1:'a',2:'b',3:'c'}
d.update({2:'d'}) # also this method use for update items
print(d)'''

'''
d={1:'a',2:'b',3:'c'}
d.clear() # remove all dict
print(d) '''

'''
d={1:'a',2:'b',3:'c'}
s=d.copy() # we copy one dict to another dict
print(d)

print(s)'''

'''
d={1:'akash',2:'ram',3:'rahul'}
d.pop(3) # direct cut 3 item
print(d)
s=d.pop() # cut last item which is available in dict
print(s)'''

'''
d={1:'akash',2:'ram',3:'rahul'}
del d[2] # totally delete item
print(d) '''

'''
d={1:'akash',2:'ram',3:'rahul'}
d.popitem() # cut key with value
print(d) '''
'''
d={1:'a',2:'b',3:'c'}
print(d.setdefault(2))
'''

'''
d=[1,2,5,3,4,2]
k={'akash'}
print(dict.fromkeys(d,k))
print(dict.fromkeys(k,d)) '''

d={1:'d'}
d[2]='f'
d[(3,4)]='j'
d[5,[6,7]]='g' # it will not allow becoz list is unhasheble
print(d)


# making dict from list items

lst=[2,4,5,6]
c=0 # for key
d={} # becoz want make dict
for i in l:
    d[c]=i #all i  will goes in dict place of c
    c+=1 # c will increase by 1
print(d)
print(type(d))





