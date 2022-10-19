def add(a=0,b=0,c=0): # formal arguments
    s=a+b+c
    return s

res1=add()
res2 = add(10)
res3=add(10,20)
res4=add(10,20,30)
print("res1 =",res1)
print("res2 =",res2)
print("res3 =",res3)
print("res4 =",res4)
print('------------------------------')
res1=add(b=33)
res2=add(c=10,a=20)
res3=add(c=10,a=20,b=30)
print("res1 =",res1)
print("res2 =",res2)
print("res3 =",res3)