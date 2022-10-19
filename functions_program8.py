def add(a,b,c=0):
    s=a+b+c
    return s

res1 = add(10,20)
res2=add(10,20,30)
print("res1 =",res1)
print("res2 =",res2)

res3=add(30,c=99,b=66)
print("res3 =",res3)
res4=add(c=33,a=22,b=88)
print("res4 =",res4)
res5 = add(b=7,a=6)
print(res5)