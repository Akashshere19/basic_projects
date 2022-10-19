'''tup=(1,2,3,'apple',5)

if (type(tup[3])==str) in tup:
        print('apple','is string element')
print(tup)

x=('apple','ball')
y=list(x)
y='cat'
x=tuple(y)
print(x)

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)

tup=('apple','ball','cat','dog')
(red,plastic,*red)=tup
print(*red)

t=("apple","ball","cat")
(red,*red)=t
print(red)
d={1:'one',2:'two',3:'three'} 
t=tuple(d)
print(t)
l=list(d)
print(l)

st=("akashshere")
for i in st:
    if "s" in i:
        print(" ")
    else:
        print(i)
s=("akash","shere")
for i in s:
    for i in i:
        if i=='s':
            print(" ")
        else:
            print(i)
t=("hello",[1,2,3],{1,2,2,3,3})
for i in t:
    print(i)
    print(type(t))

my_tuple = ('p','r','o','g','r','a','m','i','z')
print(my_tuple[::-1])
print(my_tuple)
for i in my_tuple:
    print(i,end="")'''
'''
my_tuple = ('p','r','o','g','r','a','m','i','z')
print('o'in my_tuple)'''









